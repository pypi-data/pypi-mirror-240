import torch
from torch.nn import Module, ModuleList
from torch import nn, einsum, Tensor
import torch.nn.functional as F

from einops import rearrange
from einops.layers.torch import Rearrange

from rotary_embedding_torch import RotaryEmbedding

from gateloop_transformer.associative_scan import associative_scan

# helpers

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

def safe_cumprod(t, eps = 1e-10, dim = -1):
    t = torch.clip(t, min = eps, max = 1.)
    return torch.exp(torch.cumsum(torch.log(t), dim = dim))

# rms norm

class RMSNorm(Module):
    def __init__(self, dim):
        super().__init__()
        self.scale = dim ** 0.5
        self.gamma = nn.Parameter(torch.ones(dim))

    def forward(self, x):
        return F.normalize(x, dim = -1) * self.scale * self.gamma

# feedforward

def FeedForward(dim, mult = 4):
    dim_inner = dim * mult
    return nn.Sequential(
        RMSNorm(dim),
        nn.Linear(dim, dim_inner),
        nn.GELU(),
        nn.Linear(dim_inner, dim)
    )

# attention

class CausalFullAttention(Module):
    def __init__(
        self,
        dim,
        *,
        dim_head = 64,
        heads = 8,
        data_dependent_rel_pos = False,
        frac_gradient_data_dependent_rel_pos = 0.5
    ):
        super().__init__()
        dim_inner = dim_head * heads

        self.scale = dim_head ** -0.5

        self.norm = RMSNorm(dim)

        self.to_qkv = nn.Sequential(
            nn.Linear(dim, dim_inner * 3),
            Rearrange('b n (qkv h d) -> qkv b h n d', h = heads, qkv = 3)
        )

        self.data_dependent_rel_pos = data_dependent_rel_pos
        self.frac_gradient_data_dependent_rel_pos = frac_gradient_data_dependent_rel_pos

        if data_dependent_rel_pos:
            self.to_a = nn.Sequential(
                nn.Linear(dim, dim_inner),
                Rearrange('b n (h d) -> b h n d', h = heads)
            )

            nn.init.zeros_(self.to_a[0].weight)
            nn.init.constant_(self.to_a[0].bias, 10)

        self.to_out = nn.Sequential(
            Rearrange('b h n d -> b n (h d)'),
            nn.Linear(dim_inner, dim)
        )

    def forward(self, x):
        x = self.norm(x)

        q, k, v = self.to_qkv(x)

        q = q * self.scale

        if self.data_dependent_rel_pos:
            frac_gradient = self.frac_gradient_data_dependent_rel_pos

            a = self.to_a(x)

            # allow for data dependent relative position projection to change more slowly
            # alternative to using a lowered learning rate mentioned in paper

            a = a * frac_gradient + a.detach() * (1 - frac_gradient)

            a = a.sigmoid() # not sure about this, complex formulation may be important?

            a_cumprod = safe_cumprod(a, dim = -2)
            a_cumprod_inverse = 1. / a_cumprod.clamp(min = 1e-8)

            q = q * a_cumprod
            k = k * a_cumprod_inverse

        sim = einsum('b h i d, b h j d -> b h i j', q, k)

        i, j = sim.shape[2:]
        causal_mask = torch.ones((i, j), dtype = torch.bool, device = x.device).triu(j - i + 1)

        if not self.data_dependent_rel_pos:
            sim = sim.masked_fill(causal_mask, -torch.finfo(sim.dtype).max)
            attn = sim.softmax(dim = -1)
        else:
            sim = sim.masked_fill(causal_mask, 0.)
            attn = sim

        out = einsum('b h i j, b h j d -> b h i d', attn, v)
        return self.to_out(out)

# data gated linear attention with "gateloop operator"

def gate_loop_operator(q, k, v, a):
    """
    the pseudocode in section 3.2 of the paper
    """

    kv = einsum('b n d, b n e -> b n d e', k, v)

    def binary_operator(a, b):
        a_i, kv_i = a
        a_j, kv_j = b

        # unsure, but i think this is what the paper was doing
        # feel free to open an issue if not

        a_i = a_i.real.sigmoid() + 1.j * a_i.imag
        a_j = a_j.real.sigmoid() + 1.j * a_j.imag

        return a_j * a_i, a_j.real * kv_i + kv_j

    a = rearrange(a, '... -> ... 1')
    _, kv = associative_scan(binary_operator, (a, kv), axis = 1)

    return einsum('b n d, b n d e -> b n e', q, kv)

class GateLoopedAttention(Module):
    def __init__(
        self,
        dim,
        dim_inner = None,
        frac_gradient_state_transition = 0.5
    ):
        super().__init__()
        self.frac_gradient_state_transition = frac_gradient_state_transition

        dim_inner = default(dim_inner, dim)

        self.norm = RMSNorm(dim)

        self.to_qkv = nn.Linear(dim, dim_inner * 3)

        self.to_a = nn.Sequential(
            nn.Linear(dim, dim_inner * 2),
            Rearrange('... (d c) -> ... d c', c = 2)
        )

    def forward(self, x):
        frac_gradient = self.frac_gradient_state_transition

        x = self.norm(x)

        q, k, v = self.to_qkv(x).chunk(3, dim = -1)

        a = self.to_a(x)
        a = a * frac_gradient + a.detach() * (1 - frac_gradient)

        a = torch.view_as_complex(a)

        out = gate_loop_operator(q, k, v, a)

        return out

# main class

class Transformer(Module):
    def __init__(
        self,
        dim,
        *,
        num_tokens,
        depth,
        dim_head = 64,
        heads = 8,
        ff_mult = 4,
        use_gate_looped_attn = True,
        dim_gate_looped_attn = None,
        data_dependent_rel_pos = False,
        frac_gradient_state_transition = 0.5
    ):
        super().__init__()

        self.token_emb = nn.Embedding(num_tokens, dim)

        layers = ModuleList([])

        for _ in range(depth):

            if use_gate_looped_attn:
                spatial_mixer = GateLoopedAttention(
                    dim = dim,
                    dim_inner = dim_gate_looped_attn,
                    frac_gradient_state_transition = frac_gradient_state_transition
                )
            else:
                spatial_mixer = CausalFullAttention(
                    dim = dim,
                    dim_head = dim_head,
                    heads = heads,
                    data_dependent_rel_pos = data_dependent_rel_pos,
                    frac_gradient_data_dependent_rel_pos = frac_gradient_state_transition
                )

            layers.append(ModuleList([
                spatial_mixer,
                FeedForward(
                    dim = dim,
                    mult = ff_mult
                )
            ]))

        self.layers = ModuleList(layers)

        self.to_logits = nn.Sequential(
            RMSNorm(dim),
            nn.Linear(dim, num_tokens, bias = False)
        )

    def forward(
        self,
        x,
        return_loss = False
    ):
        if return_loss:
            x, labels = x[:, :-1], x[:, 1:]

        x = self.token_emb(x)

        for attn, ff in self.layers:
            x = attn(x) + x
            x = ff(x) + x

        logits = self.to_logits(x)

        if not return_loss:
            return logits

        logits = rearrange(logits, 'b n c -> b c n')
        return F.cross_entropy(logits, labels)

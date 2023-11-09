# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Description  : 
 Version      : 1.0
 Author       : MrYXJ
 Github       : https://github.com/MrYxJ
 Date         : 2023-11-09 11:30:01
 LastEditTime : 2023-11-09 11:30:02
 Copyright (C) 2023 mryxj. All rights reserved.
'''

import torch
from torch import nn

class LlamaRotaryEmbedding(nn.Module):
    def __init__(self, dim, max_position_embeddings=4096, base=10000, device=None):
        super().__init__()

        self.dim = dim
        self.max_position_embeddings = max_position_embeddings
        self.base = base
        inv_freq = 1.0 / (self.base ** (torch.arange(0, self.dim, 2).float().to(device) / self.dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)

        # Build here to make `torch.jit.trace` work.
        self._set_cos_sin_cache(
            seq_len=max_position_embeddings, device=self.inv_freq.device, dtype=torch.get_default_dtype()
        )

    def _set_cos_sin_cache(self, seq_len, device, dtype):
        self.max_seq_len_cached = seq_len
        t = torch.arange(self.max_seq_len_cached, device=device, dtype=self.inv_freq.dtype)

        freqs = torch.einsum("i,j->ij", t, self.inv_freq)
        # Different from paper, but it uses a different permutation in order to obtain the same calculation
        emb = torch.cat((freqs, freqs), dim=-1)
        self.register_buffer("cos_cached", emb.cos().to(dtype), persistent=False)
        self.register_buffer("sin_cached", emb.sin().to(dtype), persistent=False)

    def forward(self, x, seq_len=None):
        # x: [bs, num_attention_heads, seq_len, head_size]
        if seq_len > self.max_seq_len_cached:
            self._set_cos_sin_cache(seq_len=seq_len, device=x.device, dtype=x.dtype)

        return (
            self.cos_cached[:seq_len].to(dtype=x.dtype),
            self.sin_cached[:seq_len].to(dtype=x.dtype),
        )


class LlamaLinearScalingRotaryEmbedding(nn.Module):
    """LlamaRotaryEmbedding extended with linear scaling. Credits to the Reddit user /u/kaiokendev"""

    def __init__(self, dim, max_position_embeddings=4096, base=10000, device=None, scaling_factor=1.0):
        super().__init__()
        self.scaling_factor = scaling_factor
        self.max_seq_len_cached  = max_position_embeddings
        self.base = base
        inv_freq = 1.0 / (self.base ** (torch.arange(0, dim, 2).float().to(device) / dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)
        t = torch.arange(self.max_seq_len_cached, device=device, dtype=self.inv_freq.dtype)
        t = t / self.scaling_factor

        freqs = torch.einsum("i,j->ij", t, self.inv_freq)
        # Different from paper, but it uses a different permutation in order to obtain the same calculation
        emb = torch.cat((freqs, freqs), dim=-1)
        dtype = torch.get_default_dtype()
        self.register_buffer("cos_cached", emb.cos().to(dtype), persistent=False)
        self.register_buffer("sin_cached", emb.sin().to(dtype), persistent=False)
     
    def forward(self, x, seq_len=None):
        # x: [bs, num_attention_heads, seq_len, head_size]
        # This `if` block is unlikely to be run after we build sin/cos in `__init__`. Keep the logic here just in case.
        # seq_len为序列长度，seq_len大于max_seq_len_cached，则重新计算频率矩阵，并更新cos_cached和sin_cached的缓冲区
        if seq_len > self.max_seq_len_cached:
            self.max_seq_len_cached = seq_len
            t = torch.arange(self.max_seq_len_cached, device=x.device, dtype=self.inv_freq.dtype)
            t /= self.scaling_factor
            freqs = torch.einsum("i,j->ij", t, self.inv_freq)
            
            # Different from paper, but it uses a different permutation in order to obtain the same calculation
            emb = torch.cat((freqs, freqs), dim=-1).to(x.device)
            self.register_buffer("cos_cached", emb.cos().to(x.dtype), persistent=False)
            self.register_buffer("sin_cached", emb.sin().to(x.dtype), persistent=False)

        return (
            self.cos_cached[:seq_len].to(dtype=x.dtype),
            self.sin_cached[:seq_len].to(dtype=x.dtype),
        )


class LlamaNTKScalingRotaryEmbedding(torch.nn.Module):
    def __init__(self, dim, max_position_embeddings=4096, base=10000, scaling_factor=4.0, device=None):
        super().__init__()
        # 与线性插值法相比，实现更简单，scaling_factor仅用来改变base
        base = base * scaling_factor ** (dim / (dim-2))
        inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float().to(device) / dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)

        # Build here to make `torch.jit.trace` work.
        self.max_seq_len_cached = max_position_embeddings
        t = torch.arange(self.max_seq_len_cached, device=self.inv_freq.device, dtype=self.inv_freq.dtype)
        freqs = torch.einsum("i,j->ij", t, self.inv_freq)
        # Different from paper, but it uses a different permutation in order to obtain the same calculation
        emb = torch.cat((freqs, freqs), dim=-1)
        dtype = torch.get_default_dtype()
        self.register_buffer("cos_cached", emb.cos().to(dtype), persistent=False)
        self.register_buffer("sin_cached", emb.sin().to(dtype), persistent=False)

    def forward(self, x, seq_len=None):
        # x: [bs, num_attention_heads, seq_len, head_size]
        # This `if` block is unlikely to be run after we build sin/cos in `__init__`. Keep the logic here just in case.
        if seq_len > self.max_seq_len_cached:
            self.max_seq_len_cached = seq_len
            t = torch.arange(self.max_seq_len_cached, device=x.device, dtype=self.inv_freq.dtype)
            freqs = torch.einsum("i,j->ij", t, self.inv_freq)
            # Different from paper, but it uses a different permutation in order to obtain the same calculation
            emb = torch.cat((freqs, freqs), dim=-1).to(x.device)
            self.register_buffer("cos_cached", emb.cos().to(x.dtype), persistent=False)
            self.register_buffer("sin_cached", emb.sin().to(x.dtype), persistent=False)
        return (
            self.cos_cached[:seq_len].to(dtype=x.dtype),
            self.sin_cached[:seq_len].to(dtype=x.dtype),
        )


class LlamaDynamicNTKRotaryEmbedding(torch.nn.Module):
    def __init__(self, dim, max_position_embeddings=4096, base=10000, 
                 alpha=2.0, device=None):
        super().__init__()
        self.dim = dim
        self.max_position_embeddings = max_position_embeddings
        self.base = base
        self.alpha = alpha
        self.device = device
        inv_freq = 1.0 / (self.base ** (torch.arange(0, self.dim, 2).float().to(self.device) / self.dim))
        self.register_buffer("inv_freq", inv_freq, persistent=False)
        
        self.max_seq_len_cached = max_position_embeddings
        t = torch.arange(self.max_seq_len_cached, device=self.inv_freq.device, dtype=self.inv_freq.dtype)
        freqs = torch.einsum("i,j->ij", t, self.inv_freq)
        emb = torch.cat((freqs, freqs), dim=-1)
        dtype = torch.get_default_dtype()
        self.register_buffer("cos_cached", emb.cos()[None, None, :, :].to(dtype), persistent=False)
        self.register_buffer("sin_cached", emb.sin()[None, None, :, :].to(dtype), persistent=False)

    def forward(self, x, seq_len=None):
        # x: [bs, num_attention_heads, seq_len, head_size]
        # This `if` block is unlikely to be run after we build sin/cos in `__init__`. Keep the logic here just in case.
        if seq_len > self.max_seq_len_cached:
            self.max_seq_len_cached = seq_len
            #base = base * alpha ** (dim / (dim-2))
            base = self.base * (
                (self.alpha * seq_len / self.max_position_embeddings) - (self.alpha - 1)
            ) ** (self.dim / (self.dim - 2))
            inv_freq = 1.0 / (base ** (torch.arange(0, self.dim, 2).float().to(x.device) / self.dim))
            self.register_buffer("inv_freq", inv_freq, persistent=False)
            t = torch.arange(self.max_seq_len_cached, device=x.device, dtype=self.inv_freq.dtype)
            freqs = torch.einsum("i,j->ij", t, self.inv_freq)
            # Different from paper, but it uses a different permutation in order to obtain the same calculation
            emb = torch.cat((freqs, freqs), dim=-1).to(x.device)
            self.register_buffer("cos_cached", emb.cos(), persistent=False)
            self.register_buffer("sin_cached", emb.sin(), persistent=False)
        return (
            self.cos_cached[:seq_len].to(dtype=x.dtype),
            self.sin_cached[:seq_len].to(dtype=x.dtype),
        )


def replace_llama_rotary(model, max_position_embeddings=4096):
    print('Llama position encoding use rotary, max_position_embeddings: %d.' % max_position_embeddings)
    for layer in model.base_model.layers:
        origin = layer.self_attn.rotary_emb
        head_dim = model.config.hidden_size // model.config.num_attention_heads
        injector = LlamaRotaryEmbedding(head_dim,
                                        max_position_embeddings=max_position_embeddings,
                                        device=origin.inv_freq.device)
        layer.self_attn.rotary_emb = injector


def replace_llama_rotary_with_linear_scale(model, max_position_embeddings=4096, scaling_factor=1.0):
    print('Llama position encoding use linear scale rotary, max position embeddings:%d, scaling factor:%f.' % (max_position_embeddings, scaling_factor))
    for layer in model.base_model.layers:
        origin = layer.self_attn.rotary_emb
        head_dim = model.config.hidden_size // model.config.num_attention_heads
        injector = LlamaLinearScalingRotaryEmbedding(head_dim,
                                                     max_position_embeddings=max_position_embeddings,
                                                     scaling_factor=scaling_factor,
                                                     device=origin.inv_freq.device)
        layer.self_attn.rotary_emb = injector


def replace_llama_rotary_with_ntk_scale(model, max_position_embeddings=4096, scaling_factor=1.0):
    print('Llama position encoding use ntk rotary, max position embeddings:%d, scaling factor:%f.' % (max_position_embeddings, scaling_factor))
    for layer in model.base_model.layers:
        origin = layer.self_attn.rotary_emb
        head_dim = model.config.hidden_size // model.config.num_attention_heads
        injector = LlamaNTKScalingRotaryEmbedding(head_dim,
                                                  max_position_embeddings=max_position_embeddings,
                                                  scaling_factor=scaling_factor,
                                                  device=origin.inv_freq.device)
        layer.self_attn.rotary_emb = injector


def replace_llama_rotary_with_dynamic_ntk(model, max_position_embeddings=4096, alpha=2.0):
    print("Llama position encoding load dynamic ntk rotary, max position embeddings:%d, alpha:%f." % (max_position_embeddings, alpha))
    for layer in model.base_model.layers:
        origin = layer.self_attn.rotary_emb
        head_dim = model.config.hidden_size // model.config.num_attention_heads
        injector = LlamaDynamicNTKRotaryEmbedding(head_dim,
                                                  max_position_embeddings=max_position_embeddings,
                                                  alpha=alpha,
                                                  device=origin.inv_freq.device)
        layer.self_attn.rotary_emb = injector


# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Description  : 
 Version      : 1.0
 Author       : MrYXJ
 Github       : https://github.com/MrYxJ
 Date         : 2023-11-09 11:29:06
 LastEditTime : 2023-11-09 16:28:26
 Copyright (C) 2023 mryxj. All rights reserved.
'''
from .llm_enhance import enhance_all
from .llm_enhance import enhance_llama


from .llama2_position_encoding import replace_llama_rotary_with_linear_scale
from .llama2_position_encoding import replace_llama_rotary_with_ntk_scale
from .llama2_position_encoding import replace_llama_rotary_with_dynamic_ntk


def enhance_by_replace_pe(model, max_position_embeddings):
    if model.config.model_type == "llama":
        replace_llama_rotary_with_dynamic_ntk(model, max_position_embeddings=max_position_embeddings)
        print("Enhancing Llama2 long contexts by replacing Dynamic Ntk Rotary Encoding.")
    else:
        print("Now, Llama2 is adapted, other large models(baichuan2, chatglm3 etc are continue adapted, please wait...")
  

enhance_all()
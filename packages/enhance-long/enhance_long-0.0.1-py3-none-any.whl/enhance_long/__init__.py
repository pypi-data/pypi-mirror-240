# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Description  : 
 Version      : 1.0
 Author       : MrYXJ
 Github       : https://github.com/MrYxJ
 Date         : 2023-11-09 11:29:06
 LastEditTime : 2023-11-09 11:42:57
 Copyright (C) 2023 mryxj. All rights reserved.
'''


from llama2_forward import replace_llama2_attn_with_flash_attn_attn
from llama2_forward import replace_llama2_attn_with_flash_attn_and_logn_attn_train
from llama2_forward import replace_llama2_attn_with_flash_attn_and_logn_attn_predict
from llama_position_encoding import replace_llama_rotary_with_linear_scale
from llama_position_encoding import replace_llama_rotary_with_ntk_scale
from llama_position_encoding import replace_llama_rotary_with_dynamic_ntk


def enhance_long(model, mode="predict", max_position_embeddings=4096, logn=True):
    if model.model_type == "llama":
        if mode == "predict":
            if logn:
                replace_llama2_attn_with_flash_attn_and_logn_attn_predict()
            else:
                replace_llama2_attn_with_flash_attn_attn()
        elif mode == "train":
            if logn:
                replace_llama2_attn_with_flash_attn_and_logn_attn_train
            else:
                replace_llama2_attn_with_flash_attn_attn()
        replace_llama_rotary_with_dynamic_ntk(model, max_position_embeddings=max_position_embeddings)
        print("Enhancing the ability of the llama to handle long contexts successfully")
    else:
        print("Now, only llama2 is adapted, other large models(baichuan2, chatglm3 etc are continue adapted, please wait...")
        
# !usr/bin/env python
# -*- coding:utf-8 -*-

'''
 Description  : 
 Version      : 1.0
 Author       : MrYXJ
 Mail         : code_job@163.com
 Github       : https://github.com/MrYxJ
 Date         : 2023-11-09 15:50:14
 LastEditTime : 2023-11-09 15:54:49
 FilePath     : \\EnhanceLong\\enhance_long\\llm_enhance.py
 Copyright (C) 2023 mryxj. All rights reserved.
'''

from .llama2_forward import replace_llama2_attn_with_flash_attn_attn
from .llama2_forward import replace_llama2_attn_with_flash_attn_and_logn_attn_train
from .llama2_forward import replace_llama2_attn_with_flash_attn_and_logn_attn_predict


def enhance_llama(mode="predict", logn=True):
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
    print("Enhacing Llama2 alility of processing long context initialization.")


def enhance_all():
    enhance_llama()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2021/10/27 10:39:02
@Contact :   xianhe_yan@sina.com
@python  :   3.8 
'''

import base64
import hashlib

from Cryptodome.Cipher import AES
from Cryptodome.Cipher import DES

# 盐值 下面使用使用方式截取。可以直接指定
srt_key = '8&z9v0u5l4vkjvtx&h8&z9v0u5l4vkjvtx&8&z9v0u5l4vkjvtx&e+xt+ehmk6h)w)e-47+$tsli5g!@#$%^&*()+'

class base64_tools :
    ###### base64  ######
    def srt_base64(srt_obj) :
        ## 字符串转 base64
        bs = base64.b64encode(srt_obj.encode("UTF-8"))
        # bytes 转 字符串
        return str(bs,encoding="UTF-8")
    def base64_srt(srt_obj) :
        # 字符串 转 bytes
        srt_bs = bytes(srt_obj,encoding="UTF-8")
        # base64 还原
        return base64.b64decode(srt_bs).decode("utf-8")
    def get_base64(srt_obj) :
        return  bytes(srt_obj,encoding="UTF-8")
    def get_srt(bytes_obj) :
        return  str(bytes_obj,encoding="UTF-8")
    ###### base64 end  ######

class pycryptos :

    #### DES #### 
    # 使用 DES加密数据的长度须为8的的倍数
    def des_encrypt(srt) :
        srt = base64_tools.srt_base64(srt)
        keys = hashlib.md5(srt_key.encode(encoding='UTF_8')).hexdigest()[0:8]
        key = bytes(keys, encoding="utf8")

        if len(srt) % 8 != 0:
            srt = srt + " " * (8 - len(srt) % 8)
        des = DES.new(key, DES.MODE_ECB)
        pas_enc = des.encrypt(srt.encode()).hex()
        return pas_enc

    def des_decrypt(pas_en) :
        
        keys = hashlib.md5(srt_key.encode(encoding='UTF_8')).hexdigest()[0:8]
        key = bytes(keys, encoding="utf8")

        des = DES.new(key, DES.MODE_ECB)
        pas_dec = des.decrypt(bytes.fromhex(pas_en))

        dtr_dec = str(pas_dec, encoding='utf-8').replace(" ","")
        return base64_tools.base64_srt(dtr_dec)
    #### DES end #### 

    #### AES ####
    def aes_encrypt(srt) :
        srt = base64_tools.srt_base64(srt)
        keys = hashlib.md5(srt_key.encode(encoding='UTF_8')).hexdigest()[0:16]
        key = bytes(keys, encoding="utf8")
        aes =  AES.new(key,AES.MODE_CFB,key)
        return aes.encrypt(srt.encode()).hex()
    def aes_decrypt(pas_en) :
        keys = hashlib.md5(srt_key.encode(encoding='UTF_8')).hexdigest()[0:16]
        key = bytes(keys, encoding="utf8")
        aes = AES.new(key, AES.MODE_CFB, key)
        pas_en = aes.decrypt(bytes.fromhex(pas_en))
        dtr_dec = str(pas_en, encoding='utf-8')
        return base64_tools.base64_srt(dtr_dec)

if __name__ == '__main__':
    srt = "yanxa  9"
    print(f"源 :: {srt} ")

    ## 字符串转 base64
    ## bs = base64.b64encode(srt.encode("UTF-8"))
    ## # bytes 转 字符串
    ## str_obj = str(bs,encoding="UTF-8")

    ## # 字符串 转 bytes
    ## srt_bs = bytes(str_obj,encoding="UTF-8")
    ## # base64 还原
    ## obj = base64.b64decode(srt_bs).decode("utf-8")
    ## print(f"{obj}")

    # des 
    enp = pycryptos.des_encrypt(srt)
    print(f"des加密::[{enp}]")
    pas = pycryptos.des_decrypt(enp)
    print(f"des解密::[{pas}]")

    # aes
    anp = pycryptos.aes_encrypt(srt)
    print(f"aes加密::[{anp}]")
    pas = pycryptos.aes_decrypt(anp)
    print(f"aes解密::[{pas}]")


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


#### hexdec begin

base_a = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('a'),ord('a')+6)]
base_A = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('a'),ord('a')+6)]

class hexdec :
    # 反转list
    def yreverse(list):
        return list[: :-1]

    # 十六进制转十进制两位空格
    def hex2dec(hexsrt):
        hex = hexsrt.replace(' ', '')
        return (int(hex,16))

    # 十进制转十六进制两位空格
    def dec2hex(num):
        i = 1
        l = []
        if num < 0:
            return '-' + hexdec.dec2hex(abs(num))
        while True:
            num,rem = divmod(num, 16)
            l.append(base_a[rem])
            if i % 2 == 0 :
                l.append(" ")
            ｉ = i + 1
            if num == 0:
                list1 = hexdec.yreverse(l)
                del list1[0]
                return ''.join(list1)
            
#### hexdec end


#### base64_tools begin
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
#### base64_tools end

#### pycryptos begin
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
#### pycryptos begin

if __name__ == '__main__':
    srt = "yanxa  9"
    num = 3832426215
    print(f"源 :: {srt} ")
    print(f"源 :: {num} ")

    # 字符串转 base64
    # bs = base64.b64encode(srt.encode("UTF-8"))
    # # bytes 转 字符串
    # str_obj = str(bs,encoding="UTF-8")

    # # 字符串 转 bytes
    # srt_bs = bytes(str_obj,encoding="UTF-8")
    # # base64 还原
    # obj = base64.b64decode(srt_bs).decode("utf-8")
    # print(f"{obj}")

    # # des 
    # enp = pycryptos.des_encrypt(srt)
    # print(f"des加密::[{enp}]")
    # pas = pycryptos.des_decrypt(enp)
    # print(f"des解密::[{pas}]")

    # # aes
    # anp = pycryptos.aes_encrypt(srt)
    # print(f"aes加密::[{anp}]")
    # pas = pycryptos.aes_decrypt(anp)
    # print(f"aes解密::[{pas}]")

    print(f"(dec)               :: [{num}]")  
    print(f"hex(dec)            :: [{hexdec.dec2hex(num)}]")
    print(f"reversed hex        :: [{hexdec.dec2hex(num)[: :-1] }]") 
    print(f"reversed hex(dec)   :: [{hexdec.hex2dec(hexdec.dec2hex(num)[: :-1])}]")
    

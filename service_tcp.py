#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   service_tcp.py
@Time    :   2022/04/06 09:55:07
@Author  :   yxh 
@Version :   1.0
@Contact :   xianhe_yan@sina.com
'''

from socket import *
from multiprocessing import Process
import time

address = ('192.168.1.104', 8010)

def dict_synthetic(caddr,list):
    dict_sys={}
    max = 0
    ## 标准数据格式
    dict={"协议头":2,"寄存器地址":2,"寄存器元长度":2,"字节数":1,"Unix时":4,"气象站":2,"状态码":2,"空气温℃":2,"空气湿%RH":2,"PM2.5ug/m³":2,"PM10ug/m³":2,"CO2ppm":2,"气体浓":2,"大气压KPa":4,"光照度Lux":4,"噪声dB":2,"风速m/s":2,"风级":2,"风向":2,"当日雨":2,"瞬时雨":2,"昨日雨":2,"总降雨":2,"雨雪":2,"太阳总":2,"光合有":2,"紫外辐":2,"紫外指":1,"紫外等":1,"土壤温":2,"土壤湿":2,"土壤盐":2,"土壤电":2,"土壤PH":2,"土壤氮":2,"土壤磷":2,"土壤钾":2,"信号量":2,"设备编高6位":4,"设备编低８位":4,"CRC16":2}
    if len(list) != 89 :
        list=[1,70,0,0,0,40,80,56,111,173,140,0,1,0,0,0,205,0,226,0,17,0,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,90,171,3,15,187,144,4,77]
    for k,v in dict.items() :
        vv = list[max:max + v]
        max = max + v
        dict_sys[k] = "".join('%s' %id for id in vv)
    print(("%s ::本地日期 ::{　%s } \n==当前数据::{%s} \n ")%(caddr,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),dict_sys))
    pass

##有效数据
def hxe_89(newAddr,data) :
    print((" %s 源数据:: %s")%(newAddr[0],data))
    try: 
        # 固定值前六位
        for i in range(len(data)) :
            if (89 == len(data)) :
                list.append(data[i])
            else : 
                pass
    except Exception as e :
        print(("======Exception :: %s=====")%e)
    dict_synthetic(newAddr[0],list)
def main():
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    # 重复使用绑定信息,不必等待2MSL时间
    tcpSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcpSocket.bind(address)
    tcpSocket.listen(5)
    try:
        while True:
            time.sleep(0.01)
            print('开启等待')
            newData, newAddr = tcpSocket.accept()
            print('%s客户端已经连接，准备处理数据' % newAddr[0])
            p = Process(target=recv, args=(newData, newAddr))
            p.start()
            newData.close()
    finally:
        tcpSocket.close()

def recv(newData, newAddr):
    while True:
        recvData = newData.recv(2048)
        if len(recvData) > 0:
            try :
                hxe_89(newAddr,recvData)
            finally:
                pass
        else:
            print('%s客户端已经关闭' % newAddr[0])
            break
    newData.close()


# tcpSocket.close()
if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/23 16:52:00
@Contact :   xianhe_yan@sina.com
'''
import socket
from datetime import datetime
#sk = socket.socket(type=socket.SOCK_DGRAM)

sk = socket.socket(type = socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',514)#绑定端口
name = input('请输入名字: ')
while True:
    inp = input('请输入发送内容: ')#名字
    msg_str = ('Tick! The time is: %s' % datetime.now()) + inp
    sk.sendto(str(msg_str).encode('utf-8'), ip_port)
    #msg, addr = sk.recvfrom(1024)
    #print(msg.decode('utf-8'))
sk.close()
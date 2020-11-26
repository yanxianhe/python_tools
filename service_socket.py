# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/23 16:50:54
@Contact :   xianhe_yan@sina.com
'''

####server
import socket
from datetime import datetime
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('192.168.0.100', 514))
while True:
    try:
        msg, client_addr = sk.recvfrom(1024)  # udp协议不用建立链接
        mesg = msg.decode('utf-8')
        print(mesg)
        #inp = input('>>>')
        #inp = str(datetime.now())
        #sk.sendto(inp.encode('utf-8'), client_addr)
    except Exception as e:
        print(e)
sk.close()

#!/usr/bin/env python3
# coding: utf-8
'''
Create Date: 2013-03-15
'''
import os,sys,time,logging
from ping3 import ping
from datetime import datetime
from logging import handlers

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)

def ping_some_ip(host,src_addr=None):
    second = ping(host,src_addr=src_addr)
    return second

if __name__ == '__main__':
    log = Logger('RM_CHECK_IP.log',level='debug')
    
    try:
        envX = os.environ
        host = envX.get("RM_CHECK_IP")
        if (str(host) == None) :
            ghost = sys.argv[1]
            if len(ghost) == 0:
                host = 'rymap.com'
            else:
                host = ghost
        else :
            if len(str(host)) : 
                ghost = sys.argv[1]
                if len(ghost) == 0:
                    host = 'rymap.com'
                else:
                    host = ghost
    except Exception as e:
        host = 'rymap.com'

    print("*************************************")
    print("*       欢迎使用RM ping 工具           ")
    print("*       默认 ping  rymap 官网         ")
    print("*  如：测试本地到rymap.com 官网网络情况  ")
    print("*  ./RM_CHECK_IP rymap.com           ")
    print("*  记录日志在当前目录RM_CHECK_IP.log    ")
    print("*************************************")
    log.logger.info(host)
    src_addr = None
    # src_addr = '192.168.56.1'
    # 简单用法 ping地址即可，超时会返回None 否则返回耗时，单位默认是秒
    while True:
        msg = ('ping 开始时间 :: {}'.format(datetime.now()))
        log.logger.info(msg)
        result = ping_some_ip(host,src_addr)
        if result is None:
            msg = ('ping 结束时间 :: {} \n----> {} 网络不通！，耗时{}s'.format(datetime.now(),host,result))
            log.logger.info(msg)
        else:
            msg = ('ping 结束时间 :: {} \n----> {} 网络通，耗时{}s'.format(datetime.now(),host,result))
            log.logger.info(msg)
        time.sleep(1)
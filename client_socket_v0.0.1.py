# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/22 16:39:35
@Contact :   xianhe_yan@sina.com
'''

import os
import uuid
import socket
import pymysql
import logging
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging.handlers


## Ⅰ.Python的socket模块
########################################################################################################
######################################### Python的http模块发送 #########################################

######################################### Python的http模块发送 #########################################
########################################################################################################


## Ⅱ.Python的socket模块
########################################################################################################
#########################################Python的socket模块发送#########################################
def sendsocket_udp(msg_str,ip,port):
    port=port.split("/",1)[0]
    try:
        sk = socket.socket(type = socket.SOCK_DGRAM)
        ip_port = (ip,int(port))#绑定端口
        sk.sendto(str(msg_str).encode('utf-8'), ip_port)
        #msg, addr = sk.recvfrom(1024)
        #print(msg.decode('utf-8'))
    except Exception as e:
        print (e)
    finally:
        sk.close()
#########################################Python的socket模块发送#########################################
########################################################################################################
## Ⅲ.Python的logging发送模块
########################################################################################################
#####################################Python的logging模块发送记录日志#####################################
def logsend_udp(msg_str,ip,port):
    try:
        IP=ip
        Port=port.split("/",1)[0]
        logger = logging.getLogger('WebTamper')
        fh = logging.handlers.SysLogHandler((IP, int(Port)), logging.handlers.SysLogHandler.LOG_AUTH)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        # 发送数据
        logger.warning(msg_str)
        # 遇到了重复记录日志的问题没有移除handler 必须要添加
        logger.removeHandler(fh)
    except Exception as e:
        print("logging send ERROR " % e)
#####################################Python的logging模块发送记录日志#####################################
########################################################################################################
## Ⅳ.Python的pymysql发送模块
########################################################################################################
#########################################Python的数据操作 mysql#########################################
'''
数据操作 mysql The starting point
'''
class mysqlcursor (object) :
    def __init__(self) :
        mysql_host = "192.168.3.152"
        mysql_port = 3306
        mysql_username = "root"
        mysql_passwords = "root"
        mysql_dbname = "default"
        # 标识号
        self.Serialid = str(uuid.uuid1()).replace("-", "")
        # 打开数据库连接
        self.db0 = pymysql.connect(host=mysql_host,port=mysql_port,user=mysql_username,password=mysql_passwords,db=mysql_dbname,charset='utf8')
    # 查询数据返回 list 结果
    def querylist(self,temp_sql) :
        print("{%s}:: query SQL:\t{%s} " % (self.Serialid,temp_sql))
        try:
            # 使用cursor()方法获取操作游标 
            cur = self.db0.cursor()
            cur.execute(temp_sql)
            result = cur.fetchall()
            print("{%s}:: results:\t{%s}" % (self.Serialid,result))
            return (result)
        except Exception as e :
            print("querylist error ,%s " % e)
            return e
        finally:
            # 关闭指针对象
            cur.close()
            # 关闭数据库连接对象
            self.db0.close()
    # 查询数据库返回 COUNT(*)
    def querynumber(self,temp_sql) :
        print("{%s}:: query SQL:\t{%s} " % (self.Serialid,temp_sql))
        try:
            # 使用cursor()方法获取操作游标 
            cur = self.db0.cursor()
            cur.execute(temp_sql)
            result = [tuple[0] for tuple in cur.fetchall()]
            print("{%s}:: results SQL\t{%s}" % (self.Serialid,result))
            return (result)
        except Exception as e :
            print("querynumber error ,%s " % e)
            return e
        finally:
            # 关闭指针对象
            cur.close()
            # 关闭数据库连接对象
            self.db0.close()
    # 更新数据返回 true/false
    def update_tables(self,temp_sql) :
        try:
            print("{%s}:: update SQL:\t{%s} " % (self.Serialid,temp_sql))
            # 使用cursor()方法获取操作游标 
            cur = self.db0.cursor()
            cur.execute(temp_sql)
            self.db0.commit()
            print("{%s}:: results:\t{%s}" % (self.Serialid,True))
            return True
        except Exception as e :
            cur.rollback()
            print("querynumber error ,%s " % e)
            return False
        finally:
            # 关闭指针对象
            cur.close()
            # 关闭数据库连接对象
            self.db0.close()
#########################################Python的数据操作 mysql#########################################
########################################################################################################


## Ⅴ.Python的 数据操作模块
########################################################################################################
##############################################数据操作模块##############################################
## 查询配置表;在此表中status 状态 '1'的数据都同步
def query_sync_table() :
    sql = "SELECT `id`, `databases`, `tables`, `starttime`, `initrows`, `rowsnumber`, `number`, `serviceip`,`serviceport`,`status` FROM `counts`.`syncrecord`  WHERE `status` = 1 LIMIT 0, 5000;"
    query_sync_table_lists = mysqlcursor().querylist(sql)
    return(query_sync_table_lists)
## 更新标准数据
def update_standard_data(number,databases,tables) :
    sql_update = " UPDATE `counts`.`syncrecord` SET  `rowsnumber` = %s WHERE `databases` = '%s' AND `tables` = '%s'; " % (number,databases,tables)
    flg = mysqlcursor().update_tables(sql_update)
    return flg


## 更新ip数据
def update_sendserverinfo(ip,port,databases,tables) :

    if ip != None and port != None:
        sql_update = "UPDATE counts.syncrecord SET serviceip = '%s' , serviceport = '%s' WHERE 1 = 1 ; " % (ip,port)
    else: 
        sql_update = "UPDATE counts.syncrecord SET serviceip = '%s' , serviceport = '%s' WHERE `databases` = '%s' AND `tables` = '%s'; " % (ip,port,databases,tables)  
    flg = mysqlcursor().update_tables(sql_update)
    return flg

##############################################数据操作模块##############################################
########################################################################################################


## Ⅵ.Python的 业务处理模块
########################################################################################################
##############################################业务处理模块##############################################

## 查询处理需要数据同步
def process_sync_data() :
    msg = []
    server_ip = "IP"
    server_port = int("port")
    try:
        # socket 发送
        sendsocket_udp(msg,server_ip,server_port)
        # logging
        logsend_udp(msg,server_ip,server_port)
        pass
    except Exception as e:
        print(e)




##############################################业务处理模块##############################################
########################################################################################################



## Ⅶ.Python的 入口main 方法
########################################################################################################
##############################################  main 方法 ##############################################
if __name__ == '__main__':
    logging.basicConfig()
    scheduler = BlockingScheduler()
    # 3 秒一次 调用上面的 tick 方法
    #scheduler.add_job(sendudp, 'interval', seconds=3)
    scheduler.add_job(process_sync_data, 'interval',max_instances=1,seconds=3)
    try:
        scheduler.start()
    except Exception as e:
        print(e)

##############################################  main 方法 ##############################################
########################################################################################################

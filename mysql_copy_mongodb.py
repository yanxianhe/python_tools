# -*- coding: utf-8 -*-
'''
@Author:yanxianhe
@Time    :2020/11/26 17:22:53
@Contact :     xianhe_yan@sina.com
'''
# 把mysql数据库中的数据导入mongodb中
import pymysql
import pymongo

mysql_host = 'localhost'
mysql_port = 4306
mysql_user = 'root'
mysql_password = 'root'

mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_user = 'mongoadmin'
mongodb_password = 'mongoadmin'

db_name = 'fw'


# 创建mysql的数据库连接
con = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, password=mysql_password, db=db_name,charset="utf8")
# 获取游标
cur = con.cursor(cursor=pymysql.cursors.DictCursor)
# 查询表
try:
    client = pymongo.MongoClient(host=mongodb_host,port=mongodb_port,username=mongodb_user, password=mongodb_password,authMechanism='SCRAM-SHA-256')
    cur.execute('SHOW TABLES')
    table_list = cur.fetchall()
    for i in range(len(table_list)):
        table = table_list[i]['Tables_in_fw']
        cur.execute('select * from %s' % table)
        lists = cur.fetchall()
        # 创建mongodb数据库连接
        # 获取数据库
        db = client[db_name]
        for row in lists:
            print(row)
            post = db[table]
            post.insert(row)
except Exception as e:
    print(e)
finally:
    con.close()
    client.close()

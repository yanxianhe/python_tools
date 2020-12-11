# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/12/11 09:47:50
@Contact :   xianhe_yan@sina.com
'''
import os
import hashlib
from syslogs import GetLogging
from loguru import logger

# 查看MD5值
def md5sum(filename):
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())
def duplicate_files(filedir):
    all_md5 = {}
    if len(filedir.strip()) > 0 :
        if os.path.isdir(filedir) :
            filedir = os.walk(filedir)
        else :
            filedir = os.walk(os.getcwd())
            print("默认目录 : %s" % filedir)
    else :
        filedir = os.walk(os.getcwd())
        print("默认目录 : %s" % filedir)
    for i in filedir:
        tmp_dir = i[0]
        for tlie in i[2]:
            tlie = tmp_dir + "\\" + (tlie)
            md5 = md5sum(tlie)
            if md5 in all_md5.values():
                key_path = list(all_md5.keys())[list(all_md5.values()).index(md5)]
                logger.debug("重复文件 \t %s \t\n%s \t\n%s" % (md5,key_path,tlie))
                ## 删除文件名较长的文件当前将删除 屏蔽了
                if(len(key_path) < len(tlie)):
                    #os.remove(tlie)
                    if(tlie in all_md5) :
                        del all_md5[tlie]
                    logger.info("需要手动删除文件 \t %s " % (tlie))
                else :
                    #os.remove(key_path)
                    if(key_path in all_md5) :
                        del all_md5[key_path]
                    logger.info("需要手动删除文件 \t %s " % (key_path))
                pass
            else:
                all_md5[tlie] = md5
if __name__ == '__main__':

    GetLogging().get()
    # 当前win10 系统若Linux 系统需要调整一下
    directory = "E:\PRO5-20201210\DCIM"
    print("查询目录 : %s" % directory)
    duplicate_files(directory)

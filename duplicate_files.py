# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/12/11 09:47:50
@Contact :   xianhe_yan@sina.com
'''
import os
import hashlib

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
                print("已经文件      %s ====== %s" % (key_path,md5))
                print("重复文件      %s ====== %s" % (tlie,md5))
                # os.remove(tlie)
                pass
            else:
                all_md5[tlie] = md5
if __name__ == '__main__':

    # 当前win10 系统若Linux 系统需要调整一下
    directory = "E:\\PRO5-20201210"
    print("查询目录 : %s" % directory)
    duplicate_files(directory)

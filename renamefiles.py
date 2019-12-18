# -*- coding: utf-8 -*-
# @Time :2018/8/25   20:18
# @Author : ELEVEN
# @File : 011_批量重命名文件.py
# @Software: PyCharm
import os

# 1. 获取一个要重命名的文件夹的名字
folder_name = input("请输入要重命名的文件夹:")

# 2. 获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

i=0 #编号

for name in file_names:
    name1 = name.split('-')[-1]
    newname="test-"+ name1
    old_file_name = "./" + folder_name + "/" + name
    new_file_name = "./" + folder_name + "/"+str(i) + newname
    os.rename(old_file_name, new_file_name)
    print(old_file_name)
    print(new_file_name)
    i +=1

import argparse
import os

def merge(old_dir,new_dir):
    old_res_dir = old_dir+"/res"
    new_res_dir = new_dir+"/res"
    # 自己也可以指定文件夹
    dirs = []
    # 获取res下所有的文件夹
    dirs.extend(os.listdir(old_res_dir))
    for dir in dirs:
        old_child_dir = old_res_dir+"/"+dir
        new_child_dir = new_res_dir+"/"+dir
        #如果不存在文件夹
        if(not os.path.isdir(new_child_dir)):
            os.system('mkdir {dir}'.format(dir=new_child_dir))
        #列出文件夹下所有文件
        l = os.listdir(new_child_dir)
        for file in os.listdir(old_child_dir):
            #如果文件不存在
            if(file not in l):
                cp = 'cp {from_dir}/{file} {to_dir}'.format(from_dir=old_child_dir,file=file,to_dir=new_child_dir).replace("$", "\$")
                os.system(cp)
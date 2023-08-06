#该脚本用于合并资源
import argparse
import json
import merge_file
import merge_xml
import merge_public

   

def merge():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_dir")
    parser.add_argument("new_dir")
    args = parser.parse_args()
    old_dir = args.old_dir
    new_dir = args.new_dir
    merge_public.merge(old_dir,new_dir)
    merge_file.merge(old_dir,new_dir)
    merge_xml.merge(old_dir,new_dir)
if __name__ == '__main__':
    merge()
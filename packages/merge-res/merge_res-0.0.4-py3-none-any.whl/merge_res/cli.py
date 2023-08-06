#该脚本用于合并资源
import argparse
from ast import Not
import json
import merge_file
import merge_xml
import merge_public

   

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("old_dir")
    parser.add_argument("new_dir")
    parser.add_argument("option")
    args = parser.parse_args()
    old_dir = args.old_dir
    new_dir = args.new_dir
    if args.option == 'all' or args.option is None:
        merge_public.merge(old_dir,new_dir)
        merge_file.merge(old_dir,new_dir)
        merge_xml.merge(old_dir,new_dir)
    elif args.option == 'public':
        merge_public.merge(old_dir,new_dir) 
    elif args.option == 'xml':
        merge_xml.merge(old_dir,new_dir) 
    elif args.option == 'file':
        merge_file.merge(old_dir,new_dir)
        
        
if __name__ == '__main__':
    main()
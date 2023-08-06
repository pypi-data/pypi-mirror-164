import argparse
from lxml import etree
import os
#获取所有以layout或者xml开头的文件夹

files = ["strings.xml","colors.xml","arrays.xml","styles.xml","dimens.xml","attrs.xml","plurals.xml","ids.xml","integers.xml","bools.xml","drawables.xml"]

def merge(old_dir,new_dir):
    files = os.listdir(old_dir+"/res/values")
    for file in files:
        merge_one_file(old_dir,new_dir,file)
    
def merge_one_file(old_dir,new_dir,file):
    old_file = old_dir+"/res/values/"+file
    old_file = old_dir+"/res/{dir}/{file}"
    new_file = new_dir+"/res/{dir}/{file}"
    #获取所有以values开头的文件夹
    dirs = list(filter(lambda x:x.startswith('values'),os.listdir(old_dir+"/res/")))
    # key是name value是Element
    for dir in dirs:
        from_f = old_file.format(dir=dir,file=file)
        to_f = new_file.format(dir=dir,file=file)
        change = False
        if os.path.isfile(from_f) and os.path.isfile(to_f):
            dict = {}
            to_tree = etree.parse(to_f)
            for child in to_tree.getroot():
                name = child.attrib['name']
                dict[name] = child
            from_tree = etree.parse(from_f)
            for child in from_tree.getroot():
                name = child.attrib['name'] 
                if name not in dict and "APKTOOL" not in name:
                    change = True
                    to_tree.getroot().append(child)

            if change:
                xml = '<?xml version="1.0" encoding="utf-8"?>\n'
                xml +='<resources>\n'
                for child in to_tree.getroot():
                    tag = child.tag
                    text = child.text
                    xml += '    '
                    # >会被转义
                    if(tag == 'string' and '>' in str(text)):
                        xml += etree.tostring(child,encoding='utf-8',pretty_print=True).decode('utf-8').strip().replace('/>',' />').replace('&gt;','>')
                    else:
                        xml += etree.tostring(child,encoding='utf-8',pretty_print=True).decode('utf-8').strip().replace('/>',' />')
                    xml +='\n'
                xml +='</resources>'
                with open(to_f,'w') as f:
                    f.write(xml)

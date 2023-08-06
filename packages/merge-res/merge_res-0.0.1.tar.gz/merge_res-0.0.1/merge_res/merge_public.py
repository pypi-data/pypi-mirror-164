from lxml import etree


#用于存放每种类型的最大值key是类型value是最大值
max_dict = {}
#key是类型value是name的集合
name_dict= {}


def merge(old_dir,new_dir):
    old_public = old_dir+"/res/values/public.xml"
    new_public = new_dir+"/res/values/public.xml"
    #先解析新的public.xml
    print(new_public)
    new_tree = etree.parse(new_public)
    for child in new_tree.getroot():
        if(child.tag=="public" and "id" in child.attrib):
            name=child.attrib['name']
            type=child.attrib['type']
            id=child.attrib['id']
            if(type in name_dict):
                pass
            else:
                name_dict[type] = []
            name_dict[type].append(name)
            #十六进制字符串转换为转十进制的int类型
            id = int(id,16) 
            if(type in max_dict):
                if(id > int(max_dict[type].attrib['id'],16)):
                    max_dict[type] = child
            else:
                max_dict[type] = child
    old_tree = etree.parse(old_public)
    for child in old_tree.getroot():
        if(child.tag=="public" and "id" in child.attrib):
            name=child.attrib['name']
            type=child.attrib['type']
             #屏蔽APKTOOL开头的name
            if(name not in name_dict[type] and "APKTOOL" not in name):
                max = max_dict[type]
                child.set('id',str(hex(int(max.attrib['id'],16)+1)))
                max_dict[type] = child
                index=new_tree.getroot().index(max)
                new_tree.getroot().insert(index+1,child)
    #不使用ET.write()方法，因为格式和转义
    #to_tree.write(to_public,encoding="utf-8",method="xml",pretty_print=True,xml_declaration=True,with_tail=True,strip_text=False)
    xml = '<?xml version="1.0" encoding="utf-8"?>\n'
    xml += '<resources>\n'
    for child in new_tree.getroot():
        name=child.attrib['name']
        type=child.attrib['type']
        id=child.attrib['id']
        xml += '    <public type="{type}" name="{name}" id="{id}" />'.format(type=type,name=name,id=id)
        xml += '\n'
    xml += '</resources>'
    with open(new_public,'w') as f:
        f.write(xml)

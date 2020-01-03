import xml.etree.ElementTree as ET

def read_xml(xml_file): 
    img_path = tree.find("path").text
    root = tree.findall("object")
    print("写真内にあるオブジェクトの数: ", len(root))
    count = 0
    for item in root:
        count += 1
        print("===========================")
        print("=== " + str(count) + "個目のobjectの情報 ===")
        print(item.find("name").text)
        bdbox_info = item.findall("bndbox")
        for bd in bdbox_info:
            print(bd.find("xmin").text)
            print(bd.find("ymin").text)
            print(bd.find("xmax").text)
            print(bd.find("ymax").text)
    print(img_path)


if __name__ == "__main__":    
    # xml fileがあるpath
    xml_path = "/home/tani/git/coco_analytics/VOCdevkit/VOC2012/Annotations/"
    file_name = "COCO_train2014_000000000061.xml"

    # xml fileを解析
    tree = ET.parse(xml_path + file_name)
    read_xml(tree) 

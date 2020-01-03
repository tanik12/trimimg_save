import xml.etree.ElementTree as ET
import os

def get_xml_info(xml_path):
    xml_files = os.listdir(xml_path)
    print("画像の合計枚数: ", len(xml_files))
    for file_name in xml_files:
        # xml fileを解析
        tree = ET.parse(xml_path + file_name)
        img_path = tree.find("path").text
        objects = tree.findall("object")
        #print("写真内にあるオブジェクトの数: ", len(objects), ", 画像path: ", img_path) #Debug用
        for obj in objects:
            #print("===========================")                  #Debug用
            #print("=== " + str(count) + "個目のobjectの情報 ===") #Debug用
            #print(obj.find("name").text)                          #Debug用

            #オブジェクトごとのラベル名とバウンディングボックス情報を取得する。
            bdbox_info = obj.findall("bndbox")
            bd_list = []
            for bd in bdbox_info:
                xmin = bd.find("xmin").text
                ymin = bd.find("ymin").text
                xmax = bd.find("xmax").text
                ymax = bd.find("ymax").text
                bd_list += [xmin, ymin, xmax, ymax]
                #print("===========") #Debug用
                #print("object_name: ", obj.find("name").text, ", バウンディングボックス: ", bd_list) #Debug用

if __name__ == "__main__":    
    # xml fileがあるディレクトリのパス
    xml_path = "/home/tani/git/traffic_light_dataset/Anotations/"
    get_xml_info(xml_path) 

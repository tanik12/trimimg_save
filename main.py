from get_xml_info import get_xml_info
from trim_img import *

def main():
    cofirm_dir()

    # xml fileがあるディレクトリのパス
    xml_path = "/home/tani/git/traffic_light_dataset/Anotations/"
    xml_info = get_xml_info(xml_path)

    #print(xml_info[10]) #Debug用
    make_img(xml_path, xml_info)
    
if __name__ == "__main__":
    main()

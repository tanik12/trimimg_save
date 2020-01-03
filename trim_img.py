import os
import cv2

from get_xml_info import get_xml_info

#ディレクトリの存在確認をする処理。
#ないのであればディレクトリを作成。
def cofirm_dir():
    current_path = os.getcwd()
    dirpath_anno = '/trm_images'

    if not os.path.isdir(current_path + dirpath_anno):
        os.mkdir("." + dirpath_anno)

if __name__ == "__main__":
    cofirm_dir()

    # xml fileがあるディレクトリのパス
    xml_path = "/home/tani/git/traffic_light_dataset/Anotations/"
    xml_info = get_xml_info(xml_path)
    print(xml_info[10]) #Debug用


import os
import cv2
import shutil

from get_xml_info import get_xml_info

dirpath_img = '/trm_images'

#ディレクトリの存在確認をする処理。
#ないのであればディレクトリを作成。
def cofirm_dir():
    current_path = os.getcwd()
    #dirpath_anno = '/trm_images'

    if not os.path.isdir(current_path + dirpath_img):
        os.mkdir("." + dirpath_img)

#アノテーションの情報を基にトリミング
def trm_img(img_path, bdbox, trimming_flag):
    if trimming_flag:
        #ファイル名のみ抽出
        file_name = os.path.basename(img_path)
        #画像の読み込み
        im = cv2.imread(img_path, 1)

        if bdbox[3]-bdbox[1] < 128 and bdbox[2]-bdbox[0] < 128:
            #画像をトリミング
            im = im[bdbox[1]:bdbox[3], bdbox[0]:bdbox[2]]
            #resize
            im = cv2.resize(im,(128,128))
            #トリミング済みの画像を保存
            cv2.imwrite("./" + dirpath_img  + "/trm_" + file_name, im)
    else:
        pass

#トリミングして画像を保存する。
def make_img(xml_path, xml_info, desired_obj_names, trimming_flag=False):
    img_dir = "./" + dirpath_img

    for item in xml_info:
        img_path = item["img_path"]
        obj_names = item["obj_names"]

        bdboxes = item["bdoxes"]
        for idx, bdbox in enumerate(bdboxes):
            if obj_names[idx] in desired_obj_names:
                trm_img(img_path, bdbox, trimming_flag)

if __name__ == "__main__":
    desired_obj_names = ["traffic signal", "pedestrian signal"]
    cofirm_dir()
    
    # xml fileがあるディレクトリのパス
    xml_path = "/home/tani/git/traffic_light_dataset/Anotations/"
    xml_info = get_xml_info(xml_path)
    
    #print(xml_info[10]) #Debug用
    make_img(xml_path, xml_info, desired_obj_names, trimming_flag=True)

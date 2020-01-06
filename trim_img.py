import os
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import shutil

from get_xml_info import get_xml_info

dirpath_img = '/trm_images'

#ディレクトリの存在確認をする処理。
#ないのであればディレクトリを作成。
def cofirm_dir():
    current_path = os.getcwd()

    if not os.path.isdir(current_path + dirpath_img):
        os.mkdir("." + dirpath_img)

#ディレクトリの存在確認をする処理。
#ないのであればディレクトリを作成。
def cofirm_dires(desired_obj_names):
    current_path = os.getcwd()

    if not os.path.isdir(current_path + dirpath_img):
        os.mkdir("." + dirpath_img)

    for obj_name in desired_obj_names:
        if not os.path.isdir(current_path + "/" + obj_name):
            os.mkdir(obj_name)

#アノテーションの情報を基にトリミング
def trm_img(img_path, obj_name, bdbox, count, trimming_flag):
    if trimming_flag:
        #ファイル名のみ抽出
        file_name = os.path.basename(img_path)
        img_path = img_path.replace("tani", "gisen")
        #画像の読み込み
        im = cv2.imread(img_path, 1)
        height = 24
        weight = 24
        print(img_path, obj_name, bdbox[:])
        if obj_name == "traffic_signal":
            if not bdbox[2]-bdbox[0] < weight:    
                #画像をトリミング
                im = im[bdbox[1]:bdbox[3], bdbox[0]:bdbox[2]]
                #resize
                im = cv2.resize(im, (256, 256))
                #トリミング済みの画像を保存
                cv2.imwrite("./" + dirpath_img  + "/trm_" + file_name.replace(".jpg", "") + "_" + str(count) + ".jpg", im)
                cv2.imwrite("./" + obj_name  + "/trm_" + file_name.replace(".jpg", "")  + "_" + str(count) + ".jpg", im)
        else:
            if not bdbox[3]-bdbox[1] < height:
                #画像をトリミング
                im = im[bdbox[1]:bdbox[3], bdbox[0]:bdbox[2]]
                #resize
                im = cv2.resize(im, (256, 256))
                #トリミング済みの画像を保存
                cv2.imwrite("./" + dirpath_img  + "/trm_" + file_name.replace(".jpg", "") + "_" + str(count) + ".jpg", im)
                cv2.imwrite("./" + obj_name  + "/trm_" + file_name.replace(".jpg", "")  + "_" + str(count) + ".jpg", im)

        #if bdbox[3]-bdbox[1] < height or bdbox[2]-bdbox[0] < weight:
        #    pass
        #    ##画像をトリミング
        #    #im = im[bdbox[1]:bdbox[3], bdbox[0]:bdbox[2]]
        #    ##resize
        #    #im = cv2.resize(im, (height, weight))
        #    ##トリミング済みの画像を保存
        #    #cv2.imwrite("./" + dirpath_img  + "/trm_" + file_name, im)
        #else:
        #    #画像をトリミング
        #    im = im[bdbox[1]:bdbox[3], bdbox[0]:bdbox[2]]
        #    #resize
        #    im = cv2.resize(im, (height, weight))
        #    #トリミング済みの画像を保存
        #    cv2.imwrite("./" + dirpath_img  + "/trm_" + file_name.replace(".jpg", "") + "_" + str(count) + ".jpg", im)
        #    cv2.imwrite("./" + obj_name  + "/trm_" + file_name.replace(".jpg", "")  + "_" + str(count) + ".jpg", im)
    else:
        pass

#トリミングして画像を保存する。
def make_img(xml_path, xml_info, desired_obj_names, trimming_flag=False):
    for item in xml_info:
        img_path = item["img_path"]
        obj_names = item["obj_names"]

        bdboxes = item["bdoxes"]
        count = 0
        for idx, bdbox in enumerate(bdboxes):
            obj = obj_names[idx].replace(" ", "_")
            if obj in desired_obj_names:
                trm_img(img_path, obj, bdbox, count, trimming_flag)
                count += 1

if __name__ == "__main__":
    desired_obj_names = ["traffic_signal", "pedestrian_signal"]
    cofirm_dir()
    cofirm_dires(desired_obj_names)

    # xml fileがあるディレクトリのパス
    #xml_path = "/home/tani/git/traffic_light_dataset/Anotations/"
    xml_path = "/home/gisen/git/traffic_light_dataset/Anotations/"
    xml_info = get_xml_info(xml_path)
    
    #print(xml_info[10]) #Debug用
    make_img(xml_path, xml_info, desired_obj_names, trimming_flag=True)

'''
这样产生的mask的flist是每组2000张，然后手动复制5次，直10000张。
'''

import os
from imageio import imread
from PIL import Image
import argparse


def cal_ratio(img):
        num = 0
        for x in img.flatten():
                if x > 0:
                    num += 1
        return num / img.flatten().shape[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default="/home/wwt117/Desktop/testing_mask_dataset", type=str)
    args = parser.parse_args()
    folder_path = args.path

    dirs = os.listdir(folder_path)  # 返回指定路径下的文件和文件夹列表

    mask0_10 = []
    mask10_20 = []
    mask20_30 = []
    mask30_40 = []
    mask40_50 = []
    mask50_60 = []

    i = 0
    for file_item in dirs:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        img_path = folder_path + "/" + file_item
        img = imread(img_path)
        r = cal_ratio(img)
        if 0 <= r < 0.1:
            mask0_10.append(img_path)
        elif 0.1 <= r < 0.2:
            mask10_20.append(img_path)
        elif 0.2 <= r < 0.3:
            mask20_30.append(img_path)
        elif 0.3 <= r < 0.4:
            mask30_40.append(img_path)
        elif 0.4 <= r < 0.5:
            mask40_50.append(img_path)
        elif 0.5 <= r < 0.6:
            mask50_60.append(img_path)

    # 输出文件列表
    f_mask0_10 = open('masklist/mask0_10.flist', 'w')
    f_mask0_10.write("\n".join(mask0_10))
    f_mask0_10.close()
    f_mask10_20 = open('masklist/mask10_20.flist', 'w')
    f_mask10_20.write("\n".join(mask10_20))
    f_mask10_20.close()
    f_mask20_30 = open('masklist/mask20_30.flist', 'w')
    f_mask20_30.write("\n".join(mask20_30))
    f_mask20_30.close()
    f_mask30_40 = open('masklist/mask30_40.flist', 'w')
    f_mask30_40.write("\n".join(mask30_40))
    f_mask30_40.close()
    f_mask40_50 = open('masklist/mask40_50.flist', 'w')
    f_mask40_50.write("\n".join(mask40_50))
    f_mask40_50.close()
    f_mask50_60 = open('masklist/mask50_60.flist', 'w')
    f_mask50_60.write("\n".join(mask50_60))
    f_mask50_60.close()
    
    print("Process Completed !!!")

if __name__ == "__main__":
    main()
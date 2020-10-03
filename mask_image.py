import argparse
from PIL import Image
import os
import numpy as np

# mask是双线性插值得到的因此，不全为0/255，需要重新二值化
# 自定义灰度界限，大于这个值为黑色0，小于这个值为白色1
threshold = 10
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)


def mask_image(file_num, img_folder_path, img_dirs, mask_folder_path, mask_dirs, output_folder_path, table, img_size):
    for i in range(file_num):
        if i % 100 == 0:
                print("the number of processed image:", i)
        img_path = img_folder_path + '/' + img_dirs[i]
        mask_path = mask_folder_path + '/' + mask_dirs[i]
        img = Image.open(img_path).convert('RGB')
        img = img.resize((img_size[0], img_size[1]))
        img = np.asarray(img)  # H W C
        img = img.astype(np.float32)
        mask = Image.open(mask_path)
        mask = mask.point(table, '1')
        mask = np.asarray(mask)
        # mask变成三通道
        mask = np.expand_dims(mask, axis=2)
        mask = np.concatenate((mask, mask, mask), axis=-1)  # 最后一个通道拼接
        masked_img = (1 - mask) * img + mask * 255
        masked_img = Image.fromarray(np.uint8(masked_img))
        output_path = output_folder_path + '/' + img_dirs[i]
        masked_img.save(output_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default="/data/wwt/dataset/place_testset/test10000", type=str)
    parser.add_argument('--mask', default="/data/wwt/dataset/place_testset/ratio_mask", type=str)
    parser.add_argument('--output', default="/data/wwt/dataset/place_testset/masked_place", type=str)
    parser.add_argument('--img_size', default=[256, 256], type=int)

    args = parser.parse_args()

    img_folder_path = args.path
    mask_folder_path = args.mask
    output_path = args.output

    img_size = args.img_size

    img_dirs = os.listdir(img_folder_path)
    img_dirs.sort()
    img_file_num = len(img_dirs)

    mask_0_10 = mask_folder_path + '/' + 'mask_0_10'
    mask_10_20 = mask_folder_path + '/' + 'mask_10_20'
    mask_20_30 = mask_folder_path + '/' + 'mask_20_30'
    mask_30_40 = mask_folder_path + '/' + 'mask_30_40'
    mask_40_50 = mask_folder_path + '/' + 'mask_40_50'
    mask_50_60 = mask_folder_path + '/' + 'mask_50_60'

    # ----------------------------- 开始生成mask_0_10对应的image ------------------------------
    # 返回指定路径下的文件和文件夹列表
    output_0_10 = output_path + '/' + 'masked_place_0_10'
    mask_dirs = os.listdir(mask_0_10)
    mask_dirs.sort()
    mask_file_num = len(mask_dirs)
    print("img number:", img_file_num)
    print("mask number:", mask_file_num)

    if img_file_num != mask_file_num:
        file_num = min(img_file_num, mask_file_num)
    else:
        file_num = img_file_num
    print("image number to be processed:", file_num)

    mask_image(file_num, img_folder_path, img_dirs, mask_0_10, mask_dirs, output_0_10, table, img_size)

    print("mask_0_10 finished !!!")

    # ----------------------------- 开始生成mask10_20对应的image ------------------------------
    # 返回指定路径下的文件和文件夹列表
    output_10_20 = output_path + '/' + 'masked_place_10_20'
    mask_dirs = os.listdir(mask_10_20)
    mask_dirs.sort()
    mask_file_num = len(mask_dirs)
    print("img number:", img_file_num)
    print("mask number:", mask_file_num)

    if img_file_num != mask_file_num:
        file_num = min(img_file_num, mask_file_num)
    else:
        file_num = img_file_num
    print("image number to be processed:", file_num)

    mask_image(file_num, img_folder_path, img_dirs, mask_10_20, mask_dirs, output_10_20, table, img_size)

    print("mask_0_10 finished !!!")

    # ----------------------------- 开始生成mask20_30对应的image ------------------------------
    # 返回指定路径下的文件和文件夹列表
    output_20_30 = output_path + '/' + 'masked_place_20_30'
    mask_dirs = os.listdir(mask_20_30)
    mask_dirs.sort()
    mask_file_num = len(mask_dirs)
    print("img number:", img_file_num)
    print("mask number:", mask_file_num)

    if img_file_num != mask_file_num:
        file_num = min(img_file_num, mask_file_num)
    else:
        file_num = img_file_num
    print("image number to be processed:", file_num)

    mask_image(file_num, img_folder_path, img_dirs, mask_20_30, mask_dirs, output_20_30, table, img_size)

    print("mask_20_30 finished !!!")

    # ----------------------------- 开始生成mask30_40对应的image ------------------------------
    # 返回指定路径下的文件和文件夹列表
    output_30_40 = output_path + '/' + 'masked_place_30_40'
    mask_dirs = os.listdir(mask_30_40)
    mask_dirs.sort()
    mask_file_num = len(mask_dirs)
    print("img number:", img_file_num)
    print("mask number:", mask_file_num)

    if img_file_num != mask_file_num:
        file_num = min(img_file_num, mask_file_num)
    else:
        file_num = img_file_num
    print("image number to be processed:", file_num)

    mask_image(file_num, img_folder_path, img_dirs, mask_30_40, mask_dirs, output_30_40, table, img_size)

    print("mask_30_40 finished !!!")

    # ----------------------------- 开始生成mask40_50对应的image ------------------------------
    # 返回指定路径下的文件和文件夹列表
    output_40_50 = output_path + '/' + 'masked_place_40_50'
    mask_dirs = os.listdir(mask_40_50)
    mask_dirs.sort()
    mask_file_num = len(mask_dirs)
    print("img number:", img_file_num)
    print("mask number:", mask_file_num)

    if img_file_num != mask_file_num:
        file_num = min(img_file_num, mask_file_num)
    else:
        file_num = img_file_num
    print("image number to be processed:", file_num)

    mask_image(file_num, img_folder_path, img_dirs, mask_40_50, mask_dirs, output_40_50, table, img_size)

    print("mask_40_50 finished !!!")

    # ----------------------------- 开始生成mask50_60对应的image ------------------------------
    # 返回指定路径下的文件和文件夹列表
    output_50_60 = output_path + '/' + 'masked_place_50_60'
    mask_dirs = os.listdir(mask_50_60)
    mask_dirs.sort()
    mask_file_num = len(mask_dirs)
    print("img number:", img_file_num)
    print("mask number:", mask_file_num)

    if img_file_num != mask_file_num:
        file_num = min(img_file_num, mask_file_num)
    else:
        file_num = img_file_num
    print("image number to be processed:", file_num)

    mask_image(file_num, img_folder_path, img_dirs, mask_50_60, mask_dirs, output_50_60, table, img_size)

    print("mask_50_60 finished !!!")


if __name__ == "__main__":
    main()
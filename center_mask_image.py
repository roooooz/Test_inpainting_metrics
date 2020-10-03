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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default="/data/yangxue/wwt/Inpainting_testset/Imagenet/resize_imagenet_gt", type=str)
    parser.add_argument('--mask', default="fix_mask.jpg", type=str)
    parser.add_argument('--output', default="/data/yangxue/wwt/Inpainting_testset/Imagenet", type=str)
    parser.add_argument('--width', default=256, type=int)
    parser.add_argument('--height', default=256, type=int)
    args = parser.parse_args()

    img_folder_path = args.path
    mask_path = args.mask
    output_path = args.output

    img_dirs = os.listdir(img_folder_path)
    img_dirs.sort(key=lambda x: int(x[:-4]))  # 先排序 ： 该语句的作用是倒数第四位‘.’为分界线,按照左边数字从小到大排序
    img_file_num = len(img_dirs)

    # ----------------------------- 开始生成center mask对应的image ------------------------------
    # 输出文件夹
    output_folder_path = output_path + '/' + 'center_masked_imagenet'
    print("img number:", img_file_num)

    file_num = img_file_num
    mask = Image.open(mask_path)
    mask = mask.point(table, '1')
    mask = np.asarray(mask)
    # mask变成三通道
    mask = np.expand_dims(mask, axis=2)
    mask = np.concatenate((mask, mask, mask), axis=-1)  # 最后一个通道拼接

    for i in range(file_num):
        if i % 100 == 0:
                print("the number of processed image:", i)
        img_path = img_folder_path + '/' + img_dirs[i]
        img = Image.open(img_path)
        img = np.asarray(img)  # H W C
        print(img.shape)
        if len(img.shape) != 3:
            continue
        img = img.astype(np.float32)
        masked_img = (1 - mask) * img + mask * 255
        masked_img = Image.fromarray(np.uint8(masked_img))
        output_path = output_folder_path + '/' + "{:0>5d}".format(i+1) + '.png'
        masked_img.save(output_path)

    print("center mask processing finished !!!")



if __name__ == "__main__":
    main()
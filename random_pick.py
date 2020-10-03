from PIL import Image
import argparse
import os
import random


def convert_jpg(img_path, out_path, width, height):
    img = Image.open(img_path)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(out_path)
    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default="/data/yangxue/wwt/mini-ImageNet/test", type=str)
    parser.add_argument('--output', default="/data/yangxue/wwt/Inpainting_testset/Imagenet/resize_imagenet_gt", type=str)
    parser.add_argument('--number', default=10000, type=int, help="set the number of image for test")
    parser.add_argument('--width', default=256, type=int)
    parser.add_argument('--height', default=256, type=int)
    parser.add_argument('--shuffle', default=1, type=int, help="shuffle the imageset")
    args = parser.parse_args()

    folder_path = args.path
    output_path = args.output
    img_height = args.height
    img_width = args.width

    dirs = os.listdir(folder_path)  # 返回指定路径下的文件和文件夹列表
    file_num = len(dirs)
    file_name_list = []

    pick_num = args.number
    print("总图像数量:", file_num)
    if pick_num > file_num:
        pick_num = file_num
    print("需要挑选的图像数量:", pick_num)

    # 列表中随机选出pick_num数量的文件
    if args.shuffle:
        selected_file = random.sample(dirs, pick_num)
    else:
        dirs.sort(key=lambda x: int(x[:-4]))  # 先排序 ： 该语句的作用是倒数第四位‘.’为分界线,按照左边数字从小到大排序
        selected_file = dirs[:pick_num]

    iteration = 0
    # 图像处理及输出
    for file_item in selected_file:
        # 转换成绝对路径
        file_in = folder_path + "/" + file_item
        file_out = output_path + "/" + "{:0>5d}".format(iteration+1) + '.png'
        convert_jpg(file_in, file_out, img_width, img_height)
        print("number of image:", iteration)
        print('{:s} done!'.format(file_in))
        file_name_list.append(file_out)
        iteration += 1

    print("Process Completed !!!")

    # 输出文件列表
    f = open("./random_image.flist", "w")
    f.write("\n".join(file_name_list))
    f.close()

if __name__ == "__main__":
    main()



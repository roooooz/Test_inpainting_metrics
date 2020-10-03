import argparse
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mask', default="fix_mask.jpg", type=str)
    parser.add_argument('--output', default="/home/wwt117/Desktop/Inpainting_testset/ratio_mask", type=str)
    parser.add_argument('--number', default=10000, type=int)
    args = parser.parse_args()

    mask_path = args.mask
    output_path = args.output
    file_num = args.number

    # 输出文件夹
    output_folder_path = output_path + '/' + 'center_mask'

    mask = Image.open(mask_path)

    for i in range(file_num):
        if i % 100 == 0:
                print("the number of processed image:", i)
        output_path = output_folder_path + '/' + "{:0>5d}".format(i+1) + '.png'
        mask.save(output_path)

    print("center mask processing finished !!!")


if __name__ == "__main__":
    main()
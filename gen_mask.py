import shutil
import os


def main():
    mask0_10 = 'masklist/mask0_10.flist'
    mask10_20 = 'masklist/mask10_20.flist'
    mask20_30 = 'masklist/mask20_30.flist'
    mask30_40 = 'masklist/mask30_40.flist'
    mask40_50 = 'masklist/mask40_50.flist'
    mask50_60 = 'masklist/mask50_60.flist'

    out_folder0 = '/home/wwt117/Desktop/Inpainting_testset/ratio_mask/mask_0_10'
    out_folder10 = '/home/wwt117/Desktop/Inpainting_testset/ratio_mask/mask_10_20'
    out_folder20 = '/home/wwt117/Desktop/Inpainting_testset/ratio_mask/mask_20_30'
    out_folder30 = '/home/wwt117/Desktop/Inpainting_testset/ratio_mask/mask_30_40'
    out_folder40 = '/home/wwt117/Desktop/Inpainting_testset/ratio_mask/mask_40_50'
    out_folder50 = '/home/wwt117/Desktop/Inpainting_testset/ratio_mask/mask_50_60'

    if not os.path.exists(out_folder0):
        os.mkdir(out_folder0)
    if not os.path.exists(out_folder10):
        os.mkdir(out_folder10)
    if not os.path.exists(out_folder20):
        os.mkdir(out_folder20)
    if not os.path.exists(out_folder30):
        os.mkdir(out_folder30)
    if not os.path.exists(out_folder40):
        os.mkdir(out_folder40)
    if not os.path.exists(out_folder50):
        os.mkdir(out_folder50)

    f_mask0_10 = open(mask0_10)
    r0_10 = f_mask0_10.readlines()
    f_mask0_10.close()
    f_mask10_20 = open(mask10_20)
    r10_20 = f_mask10_20.readlines()
    f_mask10_20.close()
    f_mask20_30 = open(mask20_30)
    r20_30 = f_mask20_30.readlines()
    f_mask20_30.close()
    f_mask30_40 = open(mask30_40)
    r30_40 = f_mask30_40.readlines()
    f_mask30_40.close()
    f_mask40_50 = open(mask40_50)
    r40_50 = f_mask40_50.readlines()
    f_mask40_50.close()
    f_mask50_60 = open(mask50_60)
    r50_60 = f_mask50_60.readlines()
    f_mask50_60.close()

    i = 0
    for img in r0_10:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        output = out_folder0 + '/' + "{:0>5d}".format(i) + '.png'
        shutil.copyfile(img[:-1], output)  # 最后一位是换行符img[:-1]
    print("ratio 0-10 finished !!!")

    i = 0
    for img in r10_20:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        output = out_folder10 + '/' + "{:0>5d}".format(i) + '.png'
        shutil.copyfile(img[:-1], output)  # 最后一位是换行符img[:-1]
    print("ratio 10-20 finished !!!")

    i = 0
    for img in r20_30:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        output = out_folder20 + '/' + "{:0>5d}".format(i) + '.png'
        shutil.copyfile(img[:-1], output)  # 最后一位是换行符img[:-1]
    print("ratio 20-30 finished !!!")

    i = 0
    for img in r30_40:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        output = out_folder30 + '/' + "{:0>5d}".format(i) + '.png'
        shutil.copyfile(img[:-1], output)  # 最后一位是换行符img[:-1]
    print("ratio 30-40 finished !!!")

    i = 0
    for img in r40_50:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        output = out_folder40 + '/' + "{:0>5d}".format(i) + '.png'
        shutil.copyfile(img[:-1], output)  # 最后一位是换行符img[:-1]
    print("ratio 40-50 finished !!!")

    i = 0
    for img in r50_60:
        if i % 100 == 0:
                print("the number of processed image:", i)
        i += 1
        output = out_folder50 + '/' + "{:0>5d}".format(i) + '.png'
        shutil.copyfile(img[:-1], output)  # 最后一位是换行符img[:-1]
    print("ratio 50-60 finished !!!")


if __name__ == "__main__":
    main()
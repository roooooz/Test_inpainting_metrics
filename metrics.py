import numpy as np
import argparse
import matplotlib.pyplot as plt

from glob import glob
from ntpath import basename
from scipy.misc import imread
from skimage.measure import compare_ssim
from skimage.measure import compare_psnr
from skimage.color import rgb2gray
import os

def parse_args():
    parser = argparse.ArgumentParser(description='script to compute all statistics')
    parser.add_argument('--data-path', help='Path to ground truth data', type=str)
    parser.add_argument('--output-path', help='Path to output data', type=str)
    parser.add_argument('--debug', default=0, help='Debug', type=int)
    args = parser.parse_args()
    return args


def compare_mae(img_true, img_test):
    img_true = img_true.astype(np.float32)
    img_test = img_test.astype(np.float32)
    return np.sum(np.abs(img_true - img_test)) / np.sum(img_true + img_test)


args = parse_args()
for arg in vars(args):
    print('[%s] =' % arg, getattr(args, arg))

path_true = args.data_path
path_pred = args.output_path

psnr = []
ssim = []
mae = []
names = []
index = 1

# get the list of files
true_dirs = os.listdir(path_true)  # 返回指定路径下的文件和文件夹列表
#true_dirs.sort(key=lambda x: int(x[:-4]))  # 先排序 ： 该语句的作用是倒数第四位‘.’为分界线,按照左边数字从小到大排序
pred_dirs = os.listdir(path_pred)  # 返回指定路径下的文件和文件夹列表
#pred_dirs.sort(key=lambda x: int(x[:-4]))  # 先排序 ： 该语句的作用是倒数第四位‘.’为分界线,按照左边数字从小到大排序


file_num = len(true_dirs)
pred_num = len(pred_dirs)
print("gt图像数量：", file_num)
print("pred图像数量：", pred_num)
for i in range(file_num):
    true_file_path = path_true + '/' + true_dirs[i]
    pred_file_path = path_pred + '/' + pred_dirs[i]
    img_gt = (imread(true_file_path) / 255.0).astype(np.float32)
    img_pred = (imread(pred_file_path) / 255.0).astype(np.float32)

    img_gt = rgb2gray(img_gt)
    img_pred = rgb2gray(img_pred)

    if args.debug != 0:
        plt.subplot('121')
        plt.imshow(img_gt)
        plt.title('Groud truth')
        plt.subplot('122')
        plt.imshow(img_pred)
        plt.title('Output')
        plt.show()

    psnr.append(compare_psnr(img_gt, img_pred, data_range=1))
    ssim.append(compare_ssim(img_gt, img_pred, data_range=1, win_size=51))
    mae.append(compare_mae(img_gt, img_pred))
    if np.mod(index, 100) == 0:
        print(
            str(index) + ' images processed',
            "PSNR: %.4f" % round(np.mean(psnr), 4),
            "SSIM: %.4f" % round(np.mean(ssim), 4),
            "MAE: %.4f" % round(np.mean(mae), 4),
        )
    index += 1

# np.savez(args.output_path + '/metrics.npz', psnr=psnr, ssim=ssim, mae=mae, names=names)
print(
    "PSNR: %.4f" % round(np.mean(psnr), 4),
    "PSNR Variance: %.4f" % round(np.var(psnr), 4),
    "SSIM: %.4f" % round(np.mean(ssim), 4),
    "SSIM Variance: %.4f" % round(np.var(ssim), 4),
    "MAE: %.4f" % round(np.mean(mae), 4),
    "MAE Variance: %.4f" % round(np.var(mae), 4)
)

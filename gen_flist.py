import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default="/home/wwt117/Desktop/Inpainting_testset/Celeba/center_masked_celeba", type=str)
    parser.add_argument('--output', default="/home/wwt117/Desktop/Inpainting_testset", type=str)
    parser.add_argument('--flist_name', default="center_masked_celeba.flist", type=str)
    args = parser.parse_args()

    folder_path = args.path
    output_path = args.output
    flist_name = args.flist_name
    outfile_path = output_path + "/" + flist_name

    # get the list of files
    dirs = os.listdir(folder_path)  # 返回指定路径下的文件和文件夹列表
    dirs.sort(key=lambda x: int(x[:-4]))  # 先排序 ： 该语句的作用是倒数第四位‘.’为分界线,按照左边数字从小到大排序
    file_num = len(dirs)
    file_name_list = []

    print("文件数:", file_num)


    # relative path --> absolute path
    for dir_item in dirs:
        # absolute path
        dir_item = folder_path + "/" + dir_item
        # print(dir_item)
        file_name_list.append(dir_item)


    # write to file
    f = open(outfile_path, "w")
    f.write("\n".join(file_name_list))
    f.close()

    print("Written file list path : ", outfile_path)



if __name__ == "__main__":
    main()
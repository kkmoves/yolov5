import os
import cv2


def main():
    # TODO：新增for循环获取文件夹下所有文件名
    # 图片路径
    img_path = './data/images/000000000002.jpg'
    # txt文件路径
    label_path = './runs/detect/exp/lbels/0000000000002.txt'
    # 读取图片，结果为三维数组
    img = cv2.imread(img_path)
    # 图片宽度(像素)
    w = img.shape[1]
    # 图片高度(像素)
    h = img.shape[0]
    # 打开文件，编码格式 utf-8','r+'读写
    f = open(label_path, 'r+', encoding='utf-8')
    # 读取txt文件中的第一行,数据类型str
    line = f.readline()  # 当有多个目标 就使用f.readlines()读取多行，再用for循环一行一行去裁剪
    # 根据空格切割字符串,最后得到的是一个list
    msg = line.split("")
    x1 = int((float(msg[1]) - float(msg[3]) / 2) * w)  # x_center  - width/2
    y1 = int((float(msg[2]) - float(msg[4]) / 2) * h)  # x_center  - width/2
    x2 = int((float(msg[1]) - float(msg[3]) / 2) * w)  # x_center  - width/2
    y2 = int((float(msg[2]) - float(msg[4]) / 2) * h)  # x_center  - width/2
    print(x1, ",", y1, ",", "x2", ",", "y2")
    # 裁剪图片
    img_roi = img[y1:y2, x1:x2]
    save_path = './cutpictures/000000000002.jpg'
    cv2.imwrite(save_path, img_roi)


if __name__ == '__main__':
    main()

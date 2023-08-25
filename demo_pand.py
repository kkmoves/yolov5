import pandas as pd
from PIL import Image
import os


import os
import cv2
import pandas as pd

txt_dir = r'D:\Computer_Vision\yolov5-master\runs\detect\exp2\labels'
img_dir = r'D:\Computer_Vision\yolov5-master\runs\detect\exp2'
output_dir = r'D:\Computer_Vision\yolov5-master\runs\detect\exp2/output'

for txt_file in os.listdir(txt_dir):
    if txt_file.endswith('.txt'):
        # 获取txt文件名（不包括扩展名）
        txt_name = os.path.splitext(txt_file)[0]
        # 拼接对应的图片文件名（不包括扩展名）
        img_name = txt_name + '.jpg'
        # 读取图片文件
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        # 读取txt文件并获取坐标信息
        txt_path = os.path.join(txt_dir, txt_file)
        df = pd.read_csv(txt_path, header=None, names=['x1', 'y1', 'x2', 'y2'])
        for i, row in df.iterrows():
            # 裁剪图片
            x1, y1, x2, y2 = row['x1'], row['y1'], row['x2'], row['y2']
            crop_img = img[y1:y2, x1:x2]

            # y1 = int(round((h - bbox[1]) / h * ih))
            # y2 = int(round((h - bbox[3]) / h * ih))
            # x1 = int(round(bbox[0] / w * iw))
            # x2 = int(round(bbox[2] / w * iw))

            # 保存裁剪后的图片到指定文件夹中
            output_path = os.path.join(output_dir, txt_name + f'_{i}.jpg')
            cv2.imwrite(output_path, crop_img)


























# image_path = 'exp2'
# output_path = 'exp2/output'
#
# import pandas as pd
# from PIL import Image
# import os
#
#
# # 定义裁剪函数
# def crop_image(image_path, output_path, left, top, right, bottom):
#     image = Image.open(image_path)
#     cropped_image = image.crop((left, top, right, bottom))
#     cropped_image.save(output_path)
#
#
# # 设置裁剪参数
# left = 100
# top = 100
# right = 300
# bottom = 300
#
# # 获取当前目录中所有的.txt文件
# txt_files = [file for file in os.listdir('../../..') if file.endswith('.txt')]  # ../../..
#
# # 遍历每个.txt文件
# for txt_file in txt_files:
#     # 读取文本文件
#     df = pd.read_csv(txt_file, header=None, names=['file_name'])
#
#     # 遍历每个文件名并裁剪相应的图像
#     for index, row in df.iterrows():
#         file_name = row['file_name']
#         image_path = f'{file_name}.jpg'  # 构建图像文件路径
#         output_path = f'cropped_{file_name}.jpg'  # 构建裁剪后的图像保存路径
#         crop_image(image_path, output_path, left, top, right, bottom)

# # 定义裁剪函数
# def crop_image(image_path, output_path, left, top, right, bottom):
#     image = Image.open(image_path)
#     cropped_image = image.crop((left, top, right, bottom))
#     cropped_image.save(output_path)
#
#
# # 设置裁剪参数
# left = 100
# top = 100
# right = 300
# bottom = 300
#
# # 读取文本文件
# df = pd.read_csv('file.txt', header=None, names=['file_name'])
#
# # 创建保存裁剪后图片的文件夹
# output_folder = 'cropped_images'
# os.makedirs(output_folder, exist_ok=True)
#
# # 遍历每个文件名并裁剪相应的图像
# for index, row in df.iterrows():
#     file_name = row['file_name']
#     image_path = f'{file_name}.jpg'  # 构建图像文件路径
#     output_path = os.path.join(output_folder, f'{file_name}_cropped.jpg')  # 构建裁剪后的图像保存路径
#     crop_image(image_path, output_path, left, top, right, bottom)
#
# output_folder = 'cropped_images'
# os.makedirs(output_folder, exist_ok=True)

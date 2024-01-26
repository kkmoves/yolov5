
import os
import torch
from PIL import Image
# import ultralytics

# 使用 torch.hub.load 加载模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # 使用 'yolov5m' 或其他合适的模型名称

# 指定输入文件夹和输出文件夹路径
input_folder = 'D:\\Downloads\\Documents\\yolov5\\input_images'  # 替换为包含要裁剪的图像的文件夹路径
output_folder = 'D:\\Downloads\\Documents\\yolov5\\output_images'  # 替换为要保存裁剪后图像的文件夹路径

# 如果输出文件夹不存在，创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 列出输入文件夹中的所有文件
input_files = os.listdir(input_folder)

# 指定目标单词或物体的类别
target_class = 'word'  # 替换为您的目标类别名称

# 遍历输入文件夹中的所有文件
for input_file in input_files:
    if input_file.endswith('.jpg') or input_file.endswith('.png'):
        # 加载图像
        image_path = os.path.join(input_folder, input_file)
        img = Image.open(image_path)

        # 进行目标检测
        results = model(img)

        # 找到目标类别的边界框
        for det in results.pred[0]:
            if det[-1] == model.names.index(target_class):
                x1, y1, x2, y2 = map(int, det[:4])
                cropped_image = img.crop((x1, y1, x2, y2))

                # 构建保存路径
                output_path = os.path.join(output_folder, input_file)

                # 保存裁剪后的图像
                cropped_image.save(output_path)

print("裁剪完成并保存到", output_folder)























# import os
# import torch
# from torchvision import transforms
# from PIL import Image
#
# # 加载已训练的模型
# model = torch.load('D:\\Downloads\\Documents\\yolov5\\yolov5m.pt')  # 替换为您的模型
#
# # 指定输入文件夹和输出文件夹路径
# input_folder = 'D:\\Downloads\\Documents\\yolov5\\input_images'  # 替换为包含要裁剪的图像的文件夹路径
# output_folder = 'D:\\Downloads\\Documents\\yolov5\\output_images'  # 替换为要保存裁剪后图像的文件夹路径
#
# # 如果输出文件夹不存在，创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 列出输入文件夹中的所有文件
# input_files = os.listdir(input_folder)
#
# # 指定目标单词或物体的类别
# target_class = 'word'  # 替换为您的目标类别名称
#
# # 遍历输入文件夹中的所有文件
# for input_file in input_files:
#     if input_file.endswith('.jpg') or input_file.endswith('.png'):
#         # 加载图像
#         image_path = os.path.join(input_folder, input_file)
#         img = Image.open(image_path)
#
#         # 进行目标检测
#         results = model(img)
#
#         # 找到目标类别的边界框
#         for det in results.pred[0]:
#             if det[-1] == model.names.index(target_class):
#                 x1, y1, x2, y2 = map(int, det[:4])
#                 cropped_image = img.crop((x1, y1, x2, y2))
#
#                 # 构建保存路径
#                 output_path = os.path.join(output_folder, input_file)
#
#                 # 保存裁剪后的图像
#                 cropped_image.save(output_path)
#
# print("裁剪完成并保存到", output_folder)

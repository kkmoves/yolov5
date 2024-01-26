import os
from PIL import Image
# 指定包含文本文件的目录和图像文件的目录
txt_directory = "D:\\Downloads\\Documents\\yolov5\\runs\\detect\\exp3\\labels"
img_directory = "D:\\Downloads\\Documents\\yolov5\\data\\images"

# 获取文本文件和图像文件的文件列表
txt_files = os.listdir(txt_directory)
img_files = os.listdir(img_directory)

# 遍历文本文件列表并匹配图像文件
for txt_file in txt_files:
    # 构建对应的图像文件名
    img_file = os.path.splitext(txt_file)[0] + ".jpg"

    # 检查图像文件是否存在
    if img_file in img_files:
        # 现在您可以打开 txt_file 和 img_file 进行处理
        # 例如，您可以读取 txt_file 中的坐标信息，然后使用 PIL 打开 img_file 进行裁剪和处理
        # 读取坐标信息
        with open(txt_file, "r") as file:
            lines = file.readlines()

        # 解析坐标信息
        for line in lines:
            coordinates = line.strip().split()  # 假设坐标文件的格式为 "x1 y1 x2 y2"
            if len(coordinates) == 4:
                x1, y1, x2, y2 = map(int, coordinates)

                # 裁剪图片
                cropped_image = img_file.crop((x1, y1, x2, y2))

                # 保存裁剪后的图片
                output_file = "cropped_image.jpg"  # 替换为要保存的文件路径
                cropped_image.save(output_file)

        print("裁剪完成并保存到", output_file)

        # 在这里添加您的处理代码
        print(f"处理 {txt_file} 和 {img_file}")

    else:
        print(f"找不到与 {txt_file} 相对应的图像文件")


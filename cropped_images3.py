import os
from PIL import Image

# 指定包含标注文件和图像文件的目录
data_dir = "D:\\Downloads\\Documents\\yolov5\\input_images"

# 遍历指定目录下的所有文件
for filename in os.listdir(data_dir):
    if filename.endswith(".txt"):
        txt_path = os.path.join(data_dir, filename)
        image_path = os.path.join(data_dir, filename.replace(".txt", ".jpg"))  # 假设图像文件的扩展名为.jpg

        if os.path.exists(image_path):
            # 读取标注文件
            with open(txt_path, "r") as file:
                lines = file.readlines()

            # 遍历标注文件中的每一行
            for line in lines:
                parts = line.strip().split()  # 将一行拆分成坐标信息
                x1, y1, x2, y2 = map(int, parts)  # 坐标信息

                # 打开图像
                img = Image.open(image_path)

                # 裁剪图像
                cropped_img = img.crop((x1, y1, x2, y2))

                # 保存裁剪后的图像
                cropped_image_path = os.path.join(data_dir, f"cropped_{filename.replace('.txt', '.jpg')}")
                cropped_img.save(cropped_image_path)

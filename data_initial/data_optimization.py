import cv2
import numpy as np
import os
import random

# 文件夹路径
input_dir = r"dataset_split\train\northern_leaf_blight"  # 输入图像文件夹路径
output_dir = r"dataset_split\train_optim\northern_leaf_blight"  # 保存增强图像的路径
os.makedirs(output_dir, exist_ok=True)

# 获取输入文件夹中的所有图像文件
image_list = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png','.JPG'))]

# 打印出图像文件数量，确保程序没有进入死循环
print(f"Found {len(image_list)} images in {input_dir}")

# 数据增强参数
total_target = 111  # 总共增加图像
methods = 5  # 增强方法数量（旋转、翻转、亮度、模糊、锐化）
target_per_method = total_target // methods  # 每个方法生成的图像数量

# 设定旋转角度范围
rotation_range = (25, 35)  # 旋转角度范围
brightness_range = (0.7, 1.3)  # 亮度调整范围

# 增强方法
def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(img, M, (w, h))

def flip_image(img):
    return cv2.flip(img, 1)  # 水平翻转

def adjust_brightness(img, factor):
    return cv2.convertScaleAbs(img, alpha=factor, beta=0)  # 亮度调整

def blur_image(img):
    return cv2.GaussianBlur(img, (5, 5), 0)  # 轻微模糊

def sharpen_image(img):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])  # 锐化内核
    return cv2.filter2D(img, -1, kernel)  # 应用锐化

# 生成增强图像
count = 0
while count < total_target:
    for image_name in image_list:
        image_path = os.path.join(input_dir, image_name)
        img = cv2.imread(image_path)

        if img is None:
            print(f"Error loading image: {image_name}")
            continue

        # 旋转增强
        if count < target_per_method:
            angle = random.uniform(rotation_range[0], rotation_range[1])  # 随机旋转角度
            rotated_img = rotate_image(img, angle)
            save_path = os.path.join(output_dir, f"rotated_{count}.jpg")
            cv2.imwrite(save_path, rotated_img)
            print(f"保存旋转图像: {save_path}")
            count += 1

        # 水平翻转增强
        if count < 2 * target_per_method:
            flipped_img = flip_image(img)
            save_path = os.path.join(output_dir, f"flipped_{count}.jpg")
            cv2.imwrite(save_path, flipped_img)
            print(f"保存翻转图像: {save_path}")
            count += 1

        # 亮度调整增强
        if count < 3 * target_per_method:
            brightness_factor = random.uniform(brightness_range[0], brightness_range[1])  # 随机亮度
            brightened_img = adjust_brightness(img, brightness_factor)
            save_path = os.path.join(output_dir, f"brightened_{count}.jpg")
            cv2.imwrite(save_path, brightened_img)
            print(f"保存亮度调整图像: {save_path}")
            count += 1

        # 轻微模糊增强
        if count < 4 * target_per_method:
            blurred_img = blur_image(img)
            save_path = os.path.join(output_dir, f"blurred_{count}.jpg")
            cv2.imwrite(save_path, blurred_img)
            print(f"保存模糊图像: {save_path}")
            count += 1

        # 锐化增强
        if count < total_target:
            sharpened_img = sharpen_image(img)
            save_path = os.path.join(output_dir, f"sharpened_{count}.jpg")
            cv2.imwrite(save_path, sharpened_img)
            print(f"保存锐化图像: {save_path}")
            count += 1

        if count >= total_target:
            break

print(f"共生成了 {count} 张增强图像")
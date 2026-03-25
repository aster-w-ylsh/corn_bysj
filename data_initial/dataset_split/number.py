import os

# 主文件夹路径
main_dir = r"train"  # 修改为你的主文件夹路径

# 子文件夹列表
subfolders = ["common_rust", "gray_leaf_spot", "healthy_leaf", "northern_leaf_blight"]  # 你要统计的四个子文件夹

# 遍历每个子文件夹，统计图片数量
for subfolder in subfolders:
    folder_path = os.path.join(main_dir, subfolder)  # 拼接出子文件夹的完整路径
    if os.path.exists(folder_path):
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.JPG'))]  # 支持的图片格式
        print(f"{subfolder} 中有 {len(image_files)} 张图片")
    else:
        print(f"文件夹 {subfolder} 不存在")
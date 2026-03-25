import os
import shutil

source_dir = r"C:\Users\X1\PycharmProjects\corn-bysj\data_initial\dataset_split\train_optim\northern_leaf_blight"
target_dir = r"C:\Users\X1\PycharmProjects\corn-bysj\data_initial\dataset_split\train\northern_leaf_blight"

# 打印出路径，确保路径正确
print(f"Source directory: {source_dir}")
print(f"Target directory: {target_dir}")
# 创建目标文件夹（如果不存在）
os.makedirs(target_dir, exist_ok=True)

# 获取源文件夹中的所有文件
files_in_source = os.listdir(source_dir)

# 遍历源文件夹中的所有文件，并移动到目标文件夹
for file_name in files_in_source:
    source_file = os.path.join(source_dir, file_name)
    target_file = os.path.join(target_dir, file_name)
    
    # 检查文件是否存在于目标文件夹中，避免重复移动
    if not os.path.exists(target_file):
        shutil.move(source_file, target_file)
        print(f"已移动文件: {file_name} 到 {target_dir}")
    else:
        print(f"文件 {file_name} 已经存在于目标文件夹，跳过移动")

print("所有文件已成功移动！")

# **检查目标文件夹中的图像数量**
def check_image_count(folder):
    image_count = 0
    for subfolder in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):
            files = [f for f in os.listdir(subfolder_path) if f.endswith(('.jpg', '.png', '.JPG'))]
            image_count += len(files)
            print(f"{subfolder} 中有 {len(files)} 张图片")
    print(f"总共在 {folder} 中有 {image_count} 张图片")
    return image_count

# **检查目标文件夹中的文件数量**
check_image_count(target_dir)
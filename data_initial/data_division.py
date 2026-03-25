import os
import shutil

# 原始路径（你说的这个）
data_dir = r"train"

# 输出路径
output_dir = r"dataset_split"

train_ratio = 0.7
val_ratio = 0.15

# 创建目录
for split in ['train', 'val', 'test']:
    for cls in os.listdir(data_dir):
        os.makedirs(os.path.join(output_dir, split, cls), exist_ok=True)

# 开始划分
for cls in os.listdir(data_dir):
    cls_path = os.path.join(data_dir, cls)


    images = sorted(os.listdir(cls_path))

    total = len(images)
    train_end = int(total * train_ratio)
    val_end = int(total * (train_ratio + val_ratio))

    # 按顺序切分
    train_imgs = images[:train_end]        # 前70%
    val_imgs = images[train_end:val_end]   # 中间15%
    test_imgs = images[val_end:]           # 后15%

    # 复制
    for img in train_imgs:
        shutil.copy(os.path.join(cls_path, img),
                    os.path.join(output_dir, 'train', cls, img))

    for img in val_imgs:
        shutil.copy(os.path.join(cls_path, img),
                    os.path.join(output_dir, 'val', cls, img))

    for img in test_imgs:
        shutil.copy(os.path.join(cls_path, img),
                    os.path.join(output_dir, 'test', cls, img))

print("按顺序划分完成！")
print("\n===== 数据集统计 =====")

for split in ['train', 'val', 'test']:
    print(f"\n--- {split} ---")
    split_path = os.path.join(output_dir, split)

    for cls in os.listdir(split_path):
        cls_path = os.path.join(split_path, cls)

        # 只统计文件（防止有其他文件夹）
        count = len([f for f in os.listdir(cls_path)
                     if os.path.isfile(os.path.join(cls_path, f))])

        print(f"{cls}: {count} 张")
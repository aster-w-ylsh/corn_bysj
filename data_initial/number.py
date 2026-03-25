import os

train_dir = r"data_initial/train"   # 改成你的实际路径

print("===== train 集各类别图片数量 =====\n")

total = 0

for cls in os.listdir(train_dir):
    cls_path = os.path.join(train_dir, cls)

    if os.path.isdir(cls_path):
        count = len([f for f in os.listdir(cls_path)
                     if os.path.isfile(os.path.join(cls_path, f))])

        print(f"{cls}: {count} 张")
        total += count

print(f"\n总图片数: {total}")
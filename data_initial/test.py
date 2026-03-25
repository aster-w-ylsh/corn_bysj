import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
root_dir = r"C:\Users\X1\PycharmProjects\corn-bysj\data_initial"
for class_name in os.listdir(root_dir):
    class_path = os.path.join(root_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    count = 0

    for root, dirs, files in os.walk(class_path):
        images = [f for f in files if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
        count += len(images)

    print(f"{class_name}: {count} 张")
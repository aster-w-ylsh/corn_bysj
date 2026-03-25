import cv2
import os

# ===== 路径 =====
img_dir = "gray_leaf_spot"   # 原图文件夹
save_dir = "patches"         # 裁剪保存位置

os.makedirs(save_dir, exist_ok=True)

img_list = os.listdir(img_dir)

count = 0  # patch编号

for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    img = cv2.imread(img_path)

    if img is None:
        continue

    print(f"正在处理: {img_name}")

    while True:
        # 选框
        roi = cv2.selectROI("Select Lesion (Enter确认 / ESC下一张)", img, showCrosshair=True)
        x, y, w, h = roi

        # 如果没选（直接ESC）
        if w == 0 or h == 0:
            print("进入下一张\n")
            break

        patch = img[int(y):int(y+h), int(x):int(x+w)]

        save_path = os.path.join(save_dir, f"lesion_{count}.jpg")
        cv2.imwrite(save_path, patch)

        print(f"已保存: {save_path}")
        count += 1

cv2.destroyAllWindows()

print("全部完成！")
import cv2
import numpy as np
import os
import random

healthy_dir = "healthy_leaf"
patch_dir = "patches"
save_dir = "augmented_checked"

os.makedirs(save_dir, exist_ok=True)

healthy_list = [f for f in os.listdir(healthy_dir) if f.endswith(('.jpg','.png'))]
patch_list = [f for f in os.listdir(patch_dir) if f.endswith(('.jpg','.png'))]

random.shuffle(healthy_list)

i = 0
count = 0
target_num = 300

current_scale = 1.0
current_patch_idx = 0
placed_count = 0

def load_patch(idx):
    patch = cv2.imread(os.path.join(patch_dir, patch_list[idx]))
    return patch

patch = load_patch(current_patch_idx)

def mouse(event, x, y, flags, param):
    global result, current_scale, patch, placed_count

    if event == cv2.EVENT_LBUTTONDOWN:
        ph, pw = patch.shape[:2]

        patch_resized = cv2.resize(patch, None, fx=current_scale, fy=current_scale)

        h, w = patch_resized.shape[:2]

        if x-w//2 < 0 or y-h//2 < 0 or x+w//2 >= result.shape[1] or y+h//2 >= result.shape[0]:
            return

        roi = result[y-h//2:y+h//2, x-w//2:x+w//2]

        gray = cv2.cvtColor(patch_resized, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

        mask = cv2.GaussianBlur(mask, (7,7), 0)
        mask_inv = cv2.bitwise_not(mask)

        bg_part = cv2.bitwise_and(roi, roi, mask=mask_inv)
        fg_part = cv2.bitwise_and(patch_resized, patch_resized, mask=mask)

        dst = cv2.add(bg_part, fg_part)
        result[y-h//2:y+h//2, x-w//2:x+w//2] = dst

        placed_count += 1
        print(f"已放置 {placed_count} 个病斑")

    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            current_scale *= 1.1
        else:
            current_scale *= 0.9

        current_scale = max(0.2, min(current_scale, 2.0))
        print("当前大小:", round(current_scale,2))

cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse)

while count < target_num and i < len(healthy_list):

    bg = cv2.imread(os.path.join(healthy_dir, healthy_list[i]))
    i += 1

    if bg is None:
        continue

    result = bg.copy()
    placed_count = 0

    print(f"\n当前图片: {healthy_list[i-1]}")
    print("操作：左键放置 | 滚轮缩放 | a/d切换病斑 | s保存 | n跳过")

    while True:
        cv2.imshow("image", result)
        key = cv2.waitKey(1)

        if key == ord('a'):
            current_patch_idx = (current_patch_idx - 1) % len(patch_list)
            patch = load_patch(current_patch_idx)
            print("切换patch:", patch_list[current_patch_idx])

        elif key == ord('d'):
            current_patch_idx = (current_patch_idx + 1) % len(patch_list)
            patch = load_patch(current_patch_idx)
            print("切换patch:", patch_list[current_patch_idx])

        elif key == ord('s'):
            if placed_count < 3:
                print("⚠️ 至少放3个病斑！")
                continue

            save_path = os.path.join(save_dir, f"aug_{count}.jpg")
            cv2.imwrite(save_path, result)
            print(f"✅ 保存: {save_path}")
            count += 1
            break

        elif key == ord('n'):
            print("跳过")
            break

        elif key == ord('q'):
            exit()

cv2.destroyAllWindows()
print("完成")
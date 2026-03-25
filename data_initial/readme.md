# 一、数据准备
## **1.数据集获取**
从大数据平台kaggle上整理  
灰斑病（gray_leaf_spot）
    Corn or Maize Leaf Disease Dataset
    介绍：This dataset has been made using the popular PlantVillage and PlantDoc datasets. During the formation of the dataset certain images have been removed which were not found to be useful. The original authors reserve right to the respective datasets. If you use this dataset in your academic research, please credit the authors.
健康叶片（healthy）普通锈病（common_rust）大斑病（NLB）
    从plantvillage的github仓库里面下载得到
小斑病（suthern_leaf_disease）南方锈病（southern_leaf_rust）从idadp里面玉米病害图像描述数据集
https://downgit.github.io/ 下载github上的子文件夹：把链接复制以后在这个网站下载

common_rust: 1000 张  
gray_leaf_spot: 574 张  
healthy_leaf: 1000 张  
Northern_Leaf_Blight: 985 张  
暂时是这样小斑病和南方锈病还没找好😭￣へ￣

## **2.数据划分**
**7 : 1.5 : 1.5 划分数据集**
- train  
common_rust: 700 张  
gray_leaf_spot: 401 张  
healthy_leaf: 700 张  
Northern_Leaf_Blight: 689 张  

- val  
common_rust: 150 张  
gray_leaf_spot: 86 张  
healthy_leaf: 150 张  
Northern_Leaf_Blight: 148 张  

- test  
common_rust: 150 张  
gray_leaf_spot: 87 张  
healthy_leaf: 150 张  
Northern_Leaf_Blight: 148 张  
## **3.数据处理与平衡**
对于训练数据不平衡问题做出数据增强data_optimizatuon.py
旋转：图像随机旋转，角度在 25° 到 35° 之间。
水平翻转：有 50% 的概率进行水平翻转。
亮度调整：随机调整亮度，调整范围为 0.7 到 1.3。
轻微模糊：使用 高斯模糊 来稍微模糊图像，cv2.GaussianBlur 使图像更柔和。
锐化：使用 锐化内核（通常用于提高图像的边缘细节），通过 cv2.filter2D 实现。
1. 旋转（Rotation）
目的：增强模型对不同角度图像的识别能力。
参数：旋转角度范围为 25° 到 35°。
实现：对每张图像应用随机的旋转角度，以增加图像在不同方向上的多样性。
2. 水平翻转（Horizontal Flip）
目的：增加模型对左右对称物体的识别能力。
参数：50% 概率进行水平翻转。
实现：随机对图像进行水平翻转，模拟镜像对称的情况。
3. 亮度调整（Brightness Adjustment）
目的：模拟不同光照条件下的图像变化。
参数：亮度调整系数在 0.7 到 1.3 之间随机选择。
实现：随机调整图像的亮度，以适应不同光照环境下的图像识别任务。
4. 模糊（Blurring）
目的：提高模型对模糊图像的鲁棒性。
参数：使用高斯模糊，卷积核大小为 5x5。
实现：对图像进行轻微的高斯模糊处理，模拟图像模糊的场景。
5. 锐化（Sharpening）
目的：增强图像的细节和边缘信息，提高模型的细节识别能力。
参数：使用 锐化内核 对图像进行处理。
实现：应用锐化滤镜突出图像中的细节，特别是边缘部分。
- 增强的数据  
common_rust 中有 100 张图片（800）
gray_leaf_spots 中有 380+20 张图片（800）
healthy_leaf 中有 100 张图片（800）
northern_leaf_blight 中有 111 张图片（800）  

<center><strong>实验数据分布表</strong></center>


  |病害|原始数量|训练集|验证集|测试集|  
  |:---:|:--:|:---:|:---:|:---:|
  |common_rust|1000|800|150|150|  
  |gray_leaf_spot|574|800|86|87|  
  |northern_leaf_blight|985|800|148|148|  
  |healthy_leaf|1000|800|150|150|  
import cv2
import numpy as np

# 读取图像
image = cv2.imread('number.jpg')

# 将图像转换为灰度图
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 创建拉普拉斯金字塔
pyramid = [gray_image]
for i in range(10):  # 创建4级金字塔，您可以根据需要调整级别
    gray_image = cv2.pyrDown(gray_image)  # 降采样
    pyramid.append(gray_image)

# 从金字塔的底层开始，逐渐重建图像并增强
enhanced_image = pyramid[-1]
for i in range(len(pyramid) - 2, -1, -1):
    expanded_image = cv2.pyrUp(enhanced_image)  # 上采样
    expanded_image = cv2.resize(expanded_image, pyramid[i].shape[:2][::-1])
    enhanced_image = cv2.add(pyramid[i], expanded_image)

# 显示原始图像和增强后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

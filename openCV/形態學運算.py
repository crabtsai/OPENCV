# ch12_19.py
import cv2
import numpy as np

src = cv2.imread("temple.jpg")

#開運算 先腐蝕 再膨脹
# kernel = np.ones((3,3),np.uint8)                    # 建立3x3內核
# dst = cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel)   # 開運算

#閉運算 先膨脹 在腐蝕

# kernel = np.ones((11,11),np.uint8)                  # 建立11x11內核
# dst = cv2.morphologyEx(src,cv2.MORPH_CLOSE,kernel)  # 閉運算


# 黑帽運算 原影像減去 閉運算的影像
kernel = np.ones((15,15),np.uint8)                      # 建立11x11內核
dst = cv2.morphologyEx(src,cv2.MORPH_BLACKHAT,kernel)   # blackhat

#梯度邊緣運算 獲得影像邊緣 理論 => 膨脹的影像減去腐蝕的影像
# kernel = np.ones((5,5),np.uint8)                        # 建立5x5內核
# dst = cv2.morphologyEx(src,cv2.MORPH_GRADIENT,kernel)   # gradient


#禮帽運算 原影像減去 開運算的影像
# kernel = np.ones((3,3),np.uint8)                    # 建立3x3內核
# dst = cv2.morphologyEx(src,cv2.MORPH_TOPHAT,kernel) # tophat





cv2.imshow("src",src)
cv2.imshow("after blackhat",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()




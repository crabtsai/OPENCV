# ch15_22.py
import cv2
##此方法旋轉圖像 也能匹配 0~1 數值越低越像
src = cv2.imread("myheart.jpg")
cv2.imshow("src",src)
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)         # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,127,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_LIST,
                      cv2.CHAIN_APPROX_SIMPLE)  

match0 = cv2.matchShapes(contours[0], contours[0],1,0)  # 輪廓0和0比較 
print(f"輪廓0和0比較 = {match0}")
match1 = cv2.matchShapes(contours[0], contours[1],1,0)  # 輪廓0和1比較
print(f"輪廓0和1比較 = {match1}")
match2 = cv2.matchShapes(contours[0], contours[2],1,0)  # 輪廓0和2比較
print(f"輪廓0和2比較 = {match2}")

cv2.waitKey(0)
cv2.destroyAllWindows()

##歐幾里得距離 去計算兩個輪廓的差異
cnt3 = contours[0]
hd = cv2.createHausdorffDistanceExtractor()             # 建立Hausdorff
match0 = hd.computeDistance(cnt1, cnt1)                 # 影像1和1比較 
print(f"影像1和1比較 = {match0}")
match1 = hd.computeDistance(cnt1, cnt2)                 # 影像1和2比較
print(f"影像1和2比較 = {match1}")
match2 =hd.computeDistance(cnt1, cnt3)                  # 影像1和3比較
print(f"影像1和3比較 = {match2}")
cv2.waitKey(0)
cv2.destroyAllWindows()
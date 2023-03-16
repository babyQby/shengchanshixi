import cv2
import numpy as np

img = cv2.imread("tablet.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(binary, kernel, iterations=10)
contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("药片数量：", len(contours))
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)  # 绘制所有轮廓
cv2.imshow("img", img)
cv2.waitKey(0)

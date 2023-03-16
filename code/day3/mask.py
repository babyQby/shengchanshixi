import cv2
import numpy as np

rgb_image = cv2.imread("image.jpg")
hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)

# 黄色
blue_low_hsv = np.array([100, 43, 46])
blue_high_hsv = np.array([124, 255, 255])
blue_mask = cv2.inRange(hsv, lowerb=blue_low_hsv, upperb=blue_high_hsv)

# 红色
red_low_hsv = np.array([0, 43, 46])
red_high_hsv = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv, lowerb=red_low_hsv, upperb=red_high_hsv)

bitwiseOr = cv2.bitwise_or(blue_mask, red_mask)
masked = cv2.bitwise_and(rgb_image, rgb_image, mask=bitwiseOr)

cv2.imshow('src', rgb_image)
cv2.imshow('blue_mask', blue_mask)
cv2.imshow('red_mask', red_mask)
cv2.imshow("OR", bitwiseOr)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

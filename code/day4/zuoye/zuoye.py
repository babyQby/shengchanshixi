import cv2
import numpy as np


def choose(image, number):
    cv2.imshow("image", image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask_one = cv2.inRange(hsv, lowerb=colors[0][0], upperb=colors[0][1])
    mask_two = cv2.inRange(hsv, lowerb=colors[1][0], upperb=colors[1][1])
    mask_three = cv2.inRange(hsv, lowerb=colors[2][0], upperb=colors[2][1])
    mask_four = cv2.inRange(hsv, lowerb=colors[3][0], upperb=colors[3][1])
    if number == 1:
        print("red")
        count(mask=mask_one)
    elif number == 2:
        print("yellow")
        count(mask=mask_two)
    elif number == 3:
        print("green")
        count(mask=mask_three)
    elif number == 4:
        print("blue")
        count(mask=mask_four)
    elif number == 5:
        print(all)
        mask = cv2.bitwise_or(mask_one, mask_two, mask_three, mask_four)
        count(mask=mask)
    else:
        print("按C继续，按ESC退出")
        return
    print("按C继续，按ESC退出")
    return


def count(mask):
    cv2.imshow("mask", mask)
    # masked = cv2.bitwise_and(image, image, mask=mask)
    # cv2.imshow("masked", masked)
    # gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    # ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    # cv2.imshow("binary", binary)
    erosion = cv2.erode(mask, kernel, iterations=3)
    contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("色块数量：", len(contours))
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)  # 绘制所有轮廓
    cv2.putText(frame, 'NUMBER:' + str(len(contours)), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0),
                3)
    i = 0
    for cnt in contours:
        i = i + 1
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
        cv2.putText(frame, str(i), (int(x - 10), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 100, 0), 2)
    cv2.imshow("img", frame)


if __name__ == "__main__":
    colors = np.array([[[0, 43, 46], [10, 255, 255]], [[26, 43, 46], [34, 255, 255]], [[35, 43, 46], [77, 255, 255]],
                       [[100, 43, 46], [124, 255, 255]]])
    kernel = np.ones((5, 5), np.uint8)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("摄像头打开错误")
        exit(1)
    print("按c截图识别，按ESC退出")
    while True:
        succ, frame = cap.read()
        if succ:
            cv2.imshow('cap:', frame)
            key = cv2.waitKey(16) & 0xFF
            if key == 27:
                break
            if key == ord('c'):
                num = int(input("请输入选项：\n1.红色\n2.黄色\n3.绿色\n4.蓝色\n5.全部\n其他退出\n"))
                print(num)
                choose(image=frame, number=num)

    cap.release()
    cv2.destroyAllWindows()

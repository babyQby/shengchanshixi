import datetime

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print('摄像头打开错误')
    exit(1)
cap.set(3, 480)
cap.set(4, 320)
while True:
    succ, frame = cap.read()
    if succ:
        cv2.imshow("cap:", frame)
        key = cv2.waitKey(16) & 0xFF
        if key == 27:
            break
        if key == ord('c'):
            c_name = datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S-%f') + '.jpg'
            cv2.imwrite("capture/" + c_name, frame)
            print("截图已保存：" + c_name)
cap.release()
cv2.destroyAllWindows()

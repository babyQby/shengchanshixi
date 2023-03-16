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
        cv2.imshow('cap:', frame)
        if cv2.waitKey(16) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()

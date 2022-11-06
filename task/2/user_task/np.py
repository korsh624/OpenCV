import numpy as np
import cv2
cap = cv2.VideoCapture(0)
bl = 100
wl = 0
wr = 0
b = 0
k = 0

while(True):
    frame = cv2.imread("C:/Opencv/2/user_task/images/0fb08761-c757-4a39-8142-8bc67c732dc9.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('th', th)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
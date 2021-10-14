import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    #ret, frame = cap.read()
    frame = cv2.imread(r"E:\IVAN\Ivan_desktop\Kvantorium\Trains\moodle\programs\test\doroga.jpg")
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.inRange(hsv, (0, 155, 188), (5, 255, 255))
    conts, heir = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if conts:
        cv2.drawContours(frame, conts, -1, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    #cv2.imshow("frame_gray", gray)
    cv2.imshow("frame_hsv", hsv)
    cv2.imshow("frame_thresh", thresh)
    #cv2.imshow("frame_conts", conts_frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
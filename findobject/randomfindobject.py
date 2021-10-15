import cv2
import numpy as np
import random
name=random.randint(1,3)
path="D:/ma/findobject/"+str(name)+".png"
print(path)
cap = cv2.VideoCapture(0)

while True:
    frame = cv2.imread(path)
    # frame = cv2.imread("D:/ma/findobject/1.png")
    # banka (108,223,118),(128,255,255)
    # ananassok (26,165,120),(33,255,246)
    # lampa (2,0,76),(34,15,238)
    # voda(0,76,127),(11,255,254)
    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    thresh_banka = cv2.inRange(hsv, (108,223,118),(128,255,255))
    conts_banka, heir_banka = cv2.findContours(thresh_banka.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    thresh_ananas = cv2.inRange(hsv, (26,165,120),(33,255,246))
    conts_ananas, heir_ananas = cv2.findContours(thresh_ananas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    thresh_lampa = cv2.inRange(hsv, (2,0,76),(34,15,238))
    conts_lampa, heir_lampa = cv2.findContours(thresh_lampa.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    thresh_voda = cv2.inRange(hsv, (0,76,127),(11,255,254))
    conts_voda, heir_voda = cv2.findContours(thresh_voda.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    if conts_banka:
        cv2.drawContours(frame, conts_banka, -1, (0, 255, 0), 2)
        print("banka")

    if conts_ananas:
        cv2.drawContours(frame, conts_ananas, -1, (255, 255, 0), 2)
        print("ananas")

    # if conts_lampa:
    #     cv2.drawContours(frame, conts_lampa, -1, (255, 0, 0), 2)
    #     print("lampa")

    if conts_voda:
        cv2.drawContours(frame, conts_voda, -1, (0, 255, 0), 2)
        print("voda")

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
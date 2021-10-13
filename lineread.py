import numpy as np
import cv2
cap = cv2.VideoCapture(0)
bl = 100
wl = 0
wr = 0
b = 0
k = 0

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    cols = len(th[0, :])
    rows = len(th[:, 0])
    z = cv2.waitKey(1)
    while k < 10:
            for i in range(cols):
                if b < 50 and th[k, i] == 255:
                    wl = wl + 1
                elif th[k, i] == 0:
                    b = b + 1
                elif b > 50 and th[k, i] == 255:
                    wr = wr + 1
                else:
                    continue
            #print cols, rows
            #print wl, b, wr
            spcor = (wl - wr)/4
            wl = 0
            wr = 0
            b = 0
            k = k+1
    k = 0
    #spcor = "speed corr:"+str(spcor)
    #cv2.imshow('Video', frame)
    #cv2.imshow('Frame', gray)
    cv2.imshow('w', th)
    #print(frame)
    #print(gray)
    print (spcor)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()



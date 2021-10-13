import numpy as np
import cv2 
i=0
j=0
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #blu = cv2.GaussianBlur(frame, (51, 51), 0)
    #cv2.rectangle(frame, (150, 100), (500, 200), (0, 255, 255), 2)
    i=i+1
    j=j+10
    text2=str(j)
    text=str(i)
    text=text+" data "+text2

    cv2.putText(frame,text , (10, 100),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) 
    #ret, threshold_image = cv2.threshold(gray_image, 127, 255, 0)
    #cv2.imshow('binar',threshold_image)
    #cv2.imshow('g',gray_image)
    cv2.imshow('o', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
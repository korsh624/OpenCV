import cv2
while(True):
    #ret,frame = cap.read()
    frame = cv2.imread("D:/py/x.jpg")
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)# перевод в hsv
    hsv=cv2.blur(hsv,(5,5))# размываем
    mask=cv2.inRange(hsv,(31,102,135),(73,244,231))
    
    mask=cv2.erode(mask, None, iterations=2)# Уменьшаем рябь
    mask=cv2.dilate(mask, None, iterations=4)# Большие белые объекты убираем черную рябь
    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
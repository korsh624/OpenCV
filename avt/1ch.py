import cv2
def nothing(x):
    pass

i=0
cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    #frame = cv2.imread("D:/py/x.jpg")
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)# перевод в hsv
    hsv=cv2.blur(hsv,(5,5))# размываем
    mask=cv2.inRange(hsv,(4,107,202),(28,213,255))
    cv2.imshow('mask',mask)
    mask=cv2.erode(mask, None, iterations=2)# Уменьшаем рябь
    mask=cv2.dilate(mask, None, iterations=4)# Большие белые объекты убираем черную рябь
    cv2.imshow("Mask2",mask)
    contours=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)# чб картинка, иерархия контуров, хранить контур с формате массива пикселей
    contours=contours[0]# Убираем лишнюю информацию из предыдущей функции
    if contours:
        print (contours)
        cv2.drawContours(frame,contours,-1,(255,0,255),3)#изображение на котором рисуем, массив контуров, ид контура(если нет то -1), цвет, толщина
    cv2.imshow('Contours',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
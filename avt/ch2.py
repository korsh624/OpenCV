import cv2 
cap=cv2.VideoCapture(0)
noDrive=cv2.imread("D:/python_files/avt/nodrive.png")
pedistrain=cv2.imread("D:/python_files/avt/driver.jpg")
noDrive=cv2.resize(noDrive,(64,64))
pedistrain=cv2.resize(pedistrain,(64,64))
noDrive=cv2.inRange(noDrive,(0,161,255),(123,255,255))
pedistrain=cv2.inRange(pedistrain,(51,100,109),(162,152,172))
cv2.imshow("noDrive",noDrive)
cv2.imshow("pedistrain",pedistrain)
while(True):
    ret,frame=cap.read()
    #frame = cv2.imread("D:/py/hg.jpg")
    cv2.imshow("Frame",frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv=cv2.blur(hsv,(5,5))
    mask=cv2.inRange(hsv,(98,68,255),(117,255,255))
    #mask=cv2.inRange(hsv,(0,55,76),(23,229,202))
    cv2.imshow("Mask",mask)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=4)
    cv2.imshow("Mask2",mask)

    contours=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours=contours[0]
    
    if contours:
        sorted(contours, key=cv2.contourArea,reverse=True)
        cv2.drawContours(frame,contours,-1,(255,0,0),3)    
        (x,y,w,h)=cv2.boundingRect(contours[0])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        print (x)
    cv2.imshow("Contours",frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
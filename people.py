import cv2
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cam=cv2.VideoCapture(0)
while(True):
    #ret,frame=cam.read()
    frame = cv2.imread("D:/py/x.jpg")
    (rects,weights)=hog.detectMultiScale(frame,winStride=(4,4))
    for(x,y,w,h),wei in zip(rects,weights):
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
cam.realease()

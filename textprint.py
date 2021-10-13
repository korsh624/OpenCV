import cv2
i=0
cap = cv2.VideoCapture(0)
while(True):
    frame = cv2.imread("D:/py/x.jpg")
    i+=1
    text=str(i)
    cv2.putText(frame,text , (10, 100),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3) # 
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
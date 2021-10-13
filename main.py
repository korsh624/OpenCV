import cv2
import time
redmin=82,216,219
redmax=186,230,246
greenmin=61,182,164
greenmax=165,215,184
bluemin=74,159,135
bluemax=135,195,220
yelowmin=13,240,61
yelowmax=60,255,255
colormas=[]
done=True

def findxcolor(colmin,colmax):
    frame = cv2.imread("D:/python_files/shablon.jpg")
    cv2.imshow("Frame",frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv=cv2.blur(hsv,(5,5))
    mask=cv2.inRange(hsv,(colmin),(colmax))
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
        cv2.imshow("Contours",frame)
        return x
        time.sleep(1)
while(done==True):
    x=findxcolor(greenmin,greenmax)
    print(x)
    colormas.append((x,'green'))

    x=findxcolor(bluemin,bluemax)
    print(x)
    colormas.append((x,'blue'))

    x=findxcolor(redmin,redmax)
    print(x)
    colormas.append((x,'red'))

    x=findxcolor(yelowmin,yelowmax)
    print(x)
    colormas.append((x,'yelow'))

    print(colormas)
    colormas.sort()
    print(colormas)
    done=False
    if cv2.waitKey(1)==ord("q"):
        break
#cap.release()
cv2.destroyAllWindows()
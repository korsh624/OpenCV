import cv2
images=cv2.imread("C:/Opencv/2/user_task/images/0fb08761-c757-4a39-8142-8bc67c732dc9.jpg")
frame=cv2.cvtColor(images,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(images,cv2.COLOR_BGR2HSV)
frame=cv2.resize(frame,(800,600))
cv2.imshow("frame",frame)
print(frame)
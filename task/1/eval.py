# -*- coding: utf-8 -*-
import cv2
# TODO: Допишите импорт библиотек, которые собираетесь использовать
orangemin=(0,0,196)
orangemax=(120,255,255) 
redmin=(38,147,14)
redmax=(238,255,255)
def findeconts(img,colormin,colormax):
    s=0
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, colormin, colormax)
    thresh = cv2.GaussianBlur(thresh, (5, 5), 2)
    conts, heir = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if conts:
        sorted(conts, key=cv2.contourArea,reverse=True)
        cv2.drawContours(img,conts,-1,(255,0,0),3)
        (x,y,w,h)=cv2.boundingRect(conts[0])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        s=w*h
    return s


def predict_car_signal(image):
    
    """
         Функция, определяющая сигнал автомобиля на изображении
         Входные данные: изображение (bgr)
         Выходные данные: строка c названием сигнала

         Примеры вывода: "stop signal"

                         "turn signal"
    """

    # TODO: Отредактируйте эту функцию по своему усмотрению.
    # Алгоритм проверки будет вызывать функцию predict_car_signal,
    # остальные функции должны вызываться из неё.
    turn=findeconts(image,orangemin,orangemax)
    stops=findeconts(image,redmin,redmax)
    # print('turn=',turn)
    # print('stops=',stops)
    if(turn>stops):
        car_signal = "turn signal"
    else:
        car_signal = "stop signal"
    print(car_signal)
    return car_signal


    

# img=cv2.imread('C:/Opencv/1/user_task/images/39170f2b-b730-4dba-9141-06f4184f8478.jpg')
# user_signal=predict_car_signal(img)
# print(user_signal)

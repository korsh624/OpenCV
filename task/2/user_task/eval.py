# -*- coding: utf-8 -*-
import cv2
import time

# TODO: Допишите импорт библиотек, которые собираетесь использовать

def predict_number_empty_parking_places(image):
    rgbimage=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.imshow("frame",rgbimage)
    

    """
         Функция, определяющая номера свободных парковочных мест на изображении
         Входные данные: изображение (bgr)
         Выходные данные: список номеров свободных парковочных мест, в порядке возрастания

         Примеры вывода: [1, 2, 3]
                         []
                         [1]
                         [2, 3]
    """

    # TODO: Отредактируйте эту функцию по своему усмотрению.
    # Алгоритм проверки будет вызывать функцию predict_number_empty_parking_places,
    # остальные функции, если они есть, должны вызываться из неё.

    perking_places_list = []

    return perking_places_list
images=cv2.imread("C:/Opencv/2/user_task/images/0fb08761-c757-4a39-8142-8bc67c732dc9.jpg")
while True:
    predict_number_empty_parking_places(images)
    time.sleep(1)
# --  Asynchronous Transfer of Control example.
# --  Author: Dmitriy Anisimkov.
# --  License: GPL
# --
# --  Use -gnatP switch in GNAT for Win32.
#
# with Ada.Text_IO;
# with System;
#
# procedure Asynch_Transfer is
#    type Modular_Type is mod 2 ** System.Word_Size;
#
#    N : Modular_Type := 0;
#    pragma Atomic (N);
# begin
#    select
#       delay 1.0; -- Could be entry call.
#       Ada.Text_IO.Put_Line (Modular_Type'Image (N));
#
#    then abort
#       loop
#          N := N + 1;
#       end loop;
#    end select;
#
#    Ada.Text_IO.Put_Line ("Done.");
# end Asynch_Transfer;
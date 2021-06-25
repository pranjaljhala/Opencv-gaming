import cv2
import numpy as np
from pynput.keyboard import Key,Controller
keyboard= Controller()
font = cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier("Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

framewidth=640
frameheight=480
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)
#cap1=cap.copy()
#cap1=cv2.flip(cap,0)





while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imggray, 1.1, 4)
    cv2.rectangle(img,(0,0),(176,480),(0,0,255),2)
    cv2.rectangle(img,(453,0),(640,480),(0,0,255),2)
    cv2.rectangle(img, (176, 0), (453, 137), (0, 0, 255), 2)
    cv2.rectangle(img, (176, 300), (453, 480), (0, 0, 255), 2)
    print(faces)







    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if x<=176:
            #keyboard.press('a')

            cv2.putText(img, "Left", (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        elif x>=350:
            #keyboard.press('d')

            cv2.putText(img, "right", (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            keyboard.press(Key.right)
            keyboard.release(Key.left)
        elif y<=137:
            #keyboard.press('d')

            cv2.putText(img, "up", (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        elif y>=300:
            #keyboard.press('d')

            cv2.putText(img, "down", (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        else:
            cv2.putText(img, "center", (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)


    cv2.imshow("result",img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


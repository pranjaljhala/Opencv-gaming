import cv2
import numpy as np

facecascade = cv2.CascadeClassifier("Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
img = cv2.imread("lena1.png")
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces= facecascade.detectMultiScale(imggray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)
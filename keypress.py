import cv2
import numpy as np
from pynput.mouse import Button,Controller
mouse=Controller()

framewidth=640
frameheight=480
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)

mycolors=[[0,0,255,179,34,255]]

def findcolors(img):
    #font = cv2.FONT_HERSHEY_SIMPLEX
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,255])
    upper = np.array([179,34,255])
    mask= cv2.inRange( imgHSV,lower,upper )
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
    return mask






    #cv2.putText(imgResult, int(x), (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    #cv2.imshow("test",mask)


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y



def mouseplay():
    mask=findcolors(img)
    x,y=getContours(mask)
    mouse.position=(x,y)






while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    imgResult = img.copy()
    findcolors(img)
    mouseplay()
    img=cv2.flip(img,1)
    #imgResult=cv2.flip(imgResult,1)
    cv2.imshow("result", imgResult)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
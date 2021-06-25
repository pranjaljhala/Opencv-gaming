import cv2
import numpy as np
from pynput.mouse import Button,Controller
from pynput.keyboard import Key, Controller as KeyboardController

font = cv2.FONT_HERSHEY_SIMPLEX

mouse=Controller()
keyboard=KeyboardController()
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
    lower = np.array([0,179,0])
    upper = np.array([255,0,34])
    mask= cv2.inRange( imgHSV,lower,upper )
    x,y=getContours(mask)
    cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
    return mask

#def findcolors1(img):
#    imgHSV1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#    lower1 = np.array([139,65,155])
#    upper1 = np.array([179,141,255])
#    mask2= cv2.inRange( imgHSV1,lower1,upper1 )
#    x1,y1=getContours(mask2)
#    cv2.circle(imgResult,(x1,y1),10,(0,0,255),cv2.FILLED)
#    return mask2








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
#    mask2=findcolors1(img)
    mask=findcolors(img)
    x,y=getContours(mask)
#    x2,y2=getContours(mask2)
    #mouse.position=(x,y)
    if x>0 and y>0:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    return x,y






while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    imgResult = img.copy()
    imgResult= img[40:120,200:430]
    findcolors(img)
 #   findcolors1(img)
    x,y=mouseplay()
    #print(x,y)
    x,y=str(x),str(y)
    img=cv2.flip(img,1)
    #cv2.putText(imgResult,"coordinates(x,y):" , (150, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    #v2.putText(imgResult,x, (430, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    #cv2.putText(imgResult, y, (550, 150), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("result", 640,480)
    cv2.imshow("result", imgResult)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
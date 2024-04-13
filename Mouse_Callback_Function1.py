
#Mouse Call back functions

import cv2  #Import cv2 library 
import numpy as np #Numpy array for handling data

def draw(event,x,y,flags,param): #Call back function with parameters
    if event==cv2.EVENT_LBUTTONDBLCLK: #If double click mouse left button
        cv2.circle(img,(x,y),100,(125,0,155),5) #Circle is created at the position
    if event==cv2.EVENT_RBUTTONDBLCLK:#If double click mouse right button
        cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2) #Rectangle bos is created at the position


cv2.namedWindow("res")#Windows are created for displaying images,videos,visual content
img=np.zeros((512,512,3),np.uint8) #Fully black spread img by using numpy
cv2.setMouseCallback("res",draw)#setMouseCallback function for mouse events

while True:
    cv2.imshow("res",img)#dispaly the out put
    k=cv2.waitKey(1)#wait for a key press to close the window
    if k==ord('f'):
        break

cv2.destroyAllWindows()#Destroy all windows

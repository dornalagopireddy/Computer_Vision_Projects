#Drawing Functions in Opencv

import cv2#import cv2 Library
import numpy as np#import numpyLibrary
img=cv2.imread("C:/Users/GOPI REDDY/Downloads/Artistic depict ee402102-270f-4054-a84e-905134e46d57 (1).png")#Read an image
resimg=cv2.resize(img,(500,900))#resize the image
img=cv2.line(resimg,(0,0),(200,200),(182,66,245),8)#Here the line accept 5 para (img,st,en,colorcode,thick)
img=cv2.arrowedLine(img,(0,125),(255,255),(255,0,255),10)#Here the arrowesLine accept 5 para (img,st,end,color,thick)
img=cv2.rectangle(img,(184,10),(310,128),(128,0,255),8)#Here rectangle accept 5 para (img,sta_co,end_co,color,thickness
img=cv2.circle(img,(200,64),40,(214,255,0),-1)#Circle accept 5 para (img,star_co,radius,color,radius)
font=cv2.FONT_ITALIC
img=cv2.putText(img,"SITARAM",(20,500),font,4,(0,125,255),10,cv2.LINE_AA)
blank=np.zeros([512,512,3],np.uint)*255#For blank img
white=np.zeros([512,512,3],np.uint)*255#For white img

cv2.imshow("img",img)


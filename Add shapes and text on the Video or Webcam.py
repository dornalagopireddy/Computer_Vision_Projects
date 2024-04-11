#Add shapes and text on video

import cv2 #import cv2 library
import datetime#import datetime library
cap=cv2.VideoCapture(0)#Initialize webcame
print("for width==",cap.get(cv2.CAP_PROP_FRAME_WIDTH))#default width
print("for height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#default height
print("width==",cap.get(3))
print("height==",cap.get(4))
while True:#Run the program in a loop
    ret,fra=cap.read()#Read video with pic
    frame=cv2.resize=(fra,(800,600))#resize the img
    if ret==True:#Boolean value if camera is open
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL  #font type
        text="Height"+str(cap.get(4))+"width"+str(cap.get(3)) #Height and width of a webcam
        fra=cv2.putText(fra,text,(10,20),font,1,(0,120,0),1,cv2.LINE_AA) #Place text on the frame
        date_time="Date:"+str(datetime.datetime.now())#Current date and time
        fra=cv2.putText(fra,date_time,(20,50),font,1,(100,5,255),1,cv2.LINE_AA)#Place text on the frame
        cv2.imshow("frame",fra)#Show the frame 
        q=cv2.waitKey(25)#playback spped
        if q==ord("f"):
            break
cap.release()#release
cv2.destroyAllWindows()#Close the windows
    

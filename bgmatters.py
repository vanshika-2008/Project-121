import cv2
import numpy as np

Video = cv2.VideoCapture(0)
image = cv2.imread('pypic.jpeg')
while True :
    ret,frame = Video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask = cv2.inRange(frame,l_black,u_black)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    f = np.where(f==0,image,f)
    cv2.imshow('Video',frame)
    cv2.imshow('Mask',f)
    if cv2.waitKey(1)& 0xFF==ord('q') :
        break
Video.release()
#out.release()
cv2.destroyAllWindows()
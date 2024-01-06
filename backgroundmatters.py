import cv2
import time
import numpy as np
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480))
cap = cv2.VideoCapture(0)
time.sleep(2)
frame = 0
image = cv2.imread("img.jpg")
while (cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame , (640 , 480))
    image = cv2.resize(image, (640 , 480))
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask = cv2.inRange(frame,u_black,l_black)
    res = cv2.bitwise_and(frame , frame , mask = mask)

    f = frame - res
    f = np.where(f == 0 , image , f)
    cv2.imshow('Frame', f)


cap.release()
out.release()
cv2.destroyAllWindows()
 
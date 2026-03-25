import cv2
import numpy as np
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,120,70])
    upper_red=np.array([10,255,255])

    lower_blue=np.array([100,150,0])
    upper_blue=np.array([140,255,255])

    lower_green=np.array([40,40,40])
    upper_green=np.array([70,255,255])

    lower_yellow=np.array([20,100,100])
    upper_yellow=np.array([30,255,255])

    mask=cv2.inRange(hsv,lower_red,upper_red,lower_blue,upper_blue,lower_green,upper_green,lower_yellow,upper_yellow)

    kernel=np.ones((9,9),np.uint8)
    erode=cv2.erode(mask,kernel,iterations=1)
    dilate=cv2.dilate(erode,kernel,iterations=2)

    contours=cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    bounding_box=cv2.boundingRect(contours)
    x,y,w,h=bounding_box
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
    cv2.putText(frame, "RED OBJECT", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow("objec",frame)
    cv2.imshow("mask",mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
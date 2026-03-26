from fer import FER
import cv2
detector=FER()
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,frame=cap.read()
    
    result=detector.detect_emotions(frame)

    for face in result:
        x,y,w,h=face["box"]
        emotion=max(face["emotions"],key=face["emotions"].get)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.imshow("emotion detection",frame)

        if cv2.waitKey(0)==27:
            break
        cap.release()
        cv2.destroyAllWindows()
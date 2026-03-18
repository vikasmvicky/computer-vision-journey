import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 1. Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. Define blue range
    lower_blue= np.array([120,0,70])
    upper_blue = np.array([255,120,255])

    # 3. Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4. Remove noise
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # 5. Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 6. Loop through contours
    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 800:   # filter noise

            # 7. Bounding box
            x, y, w, h = cv2.boundingRect(cnt)

            # 8. Draw rectangle
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            # 9. Label
            cv2.putText(frame, "RED OBJECT", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow("Object Detection", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
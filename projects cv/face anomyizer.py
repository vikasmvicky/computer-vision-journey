import cv2

# Correct cascade file
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

# Safety check (important habit)
if face_cascade.empty():
    print("Error loading cascade file")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(face, (51, 51), 30)
        frame[y:y+h, x:x+w] = blurred

    # Show frame OUTSIDE loop
    cv2.imshow("Face Anonymizer", frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release AFTER loop
cap.release()
cv2.destroyAllWindows()
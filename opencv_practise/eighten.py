import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
if img is None:
    print("image is not found")
    exit()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
plt.imshow(thresh,cmap="gray")
plt.title("binary threshold")
plt.axis("off")
plt.show()
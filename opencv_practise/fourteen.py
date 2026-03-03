import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv_rgb=cv2.cvtColor(hsv,cv2.COLOR_BGR2RGB)
plt.imshow(hsv_rgb)
plt.title("hsv image (visualized)")
plt.axis("off")
plt.show()
#increase brightnes
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
bright_contrast=cv2.convertScaleAbs(img, alpha=1.5, beta=0)
img_rgb=cv2.cvtColor(bright_contrast,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title("brightened image")
plt.axis("off")
plt.show()
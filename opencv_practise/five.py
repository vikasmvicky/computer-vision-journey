#increase brightness
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("../computer vision/data/image.jpeg")
bright=cv2.convertScaleAbs(img,alpha=1,beta=50)
img_rgb=cv2.cvtColor(bright,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
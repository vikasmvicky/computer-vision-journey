import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
lower_red=np.array([0,120,70])
upper_red=np.array([10,255,255])
mask=cv2.inRange(img,lower_red,upper_red)
plt.imshow(mask,cmap="gray")
plt.title("mask")
plt.axis("off")
plt.show()
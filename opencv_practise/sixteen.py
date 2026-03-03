import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
lower_red=np.array([0,120,70])
upper_red=np.array([10,255,255])
mask=cv2.inRange(img,lower_red,upper_red)
result=cv2.bitwise_and(img,img,mask=mask)
result_rgb=cv2.cvtColor(result,cv2.COLOR_BGR2RGB)
plt.imshow(result_rgb)
plt.title("mask")
plt.axis("off")
plt.show()
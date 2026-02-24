import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("image.jpeg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print("shape:",img.shape)
print("data type:",img.dtype)
print("pixel at(100,100):",img[100,100])
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
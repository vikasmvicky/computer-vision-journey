#extract only red
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
red_channel=img[:,:,2]
plt.imshow(red_channel)
plt.title("red channel")
plt.show()
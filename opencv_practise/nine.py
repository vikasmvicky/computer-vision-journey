import cv2 # swap red and blue
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
swapped=img.copy()
swapped[:,:,0]=img[:,:,2]
swapped[:,:,2]=img[:,:,0]
swapped_rgb=cv2.cvtColor(swapped,cv2.COLOR_BGR2RGB)
plt.imshow(swapped_rgb)
plt.title("red-blue swapped")
plt.axis("off")
plt.show()
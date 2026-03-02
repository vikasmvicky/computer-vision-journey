import cv2 #negative image
import matplotlib.pyplot as plt
img=cv2.imread("data/image.jpeg")
negative=255-img
negative_rgb=cv2.cvtColor(negative,cv2.COLOR_BGR2RGB)
plt.imshow(negative_rgb)
plt.title("negative image")
plt.axis("off")
plt.show()

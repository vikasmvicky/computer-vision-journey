#create a small blue square manually
import cv2
from matplotlib.pylab import imag
import matplotlib.pyplot as plt
img=cv2.imread("../computer vision/data/image.jpeg")
if img is None:
    print("image not found")
    exit()
    img[100:150,100:150]=[255,0,0] #blue in bgr
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
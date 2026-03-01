#change one pixel 
import cv2
import matplotlib.pyplot as plt 
img=cv2.imread("../computer vision/data/image.jpeg") 
if img is None: 
    print("image not found")
    exit() 
    img[100,100]=[0,0,255] #bgr fromat
     #covert to rgb for display 
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis("on") 
plt.show()
#resize while keeping aspect ratio
import cv2 
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
height,width=img.shape[:2]
new_width=400
aspect_ratio=new_width/width
new_height=int(height*aspect_ratio)
resized=cv2.resize(img,(new_width,new_height))
resized_rgb=cv2.cvtColor(resized,cv2.COLOR_BGR2RGB)
plt.imshow(resized_rgb)
plt.title("resized image")
plt.show()
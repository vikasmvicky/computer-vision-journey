#crop center region
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("data/image1.jpeg")
h,w=img.shape[:2]
center_x,center_y=w//2,h//2
crop_size=400
cropped=img[center_y-crop_size//2:center_y+crop_size//2,center_x-crop_size//2:center_x+crop_size//2]
cropped_rgb=cv2.cvtColor(cropped,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped center")
plt.axis("off")
plt.show()
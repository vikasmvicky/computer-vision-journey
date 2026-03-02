import cv2 #shape,dtype,min max
import numpy as np
img=cv2.imread("data/image.jpeg")
if img is None:
    print("image not found")
    exit()
print("shape:",img.shape)
print("dtype:",img.dtype)
print("min:",img.min())
print("max:",img.max())
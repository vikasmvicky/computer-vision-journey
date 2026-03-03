import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("data/image1.jpeg")

if img is None:
    raise ValueError("Check image path")

# Step 1: Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Step 2: Define red range
lower_red1 = np.array([0,120,70])
upper_red1 = np.array([10,255,255])

lower_red2 = np.array([170,120,70])
upper_red2 = np.array([179,255,255])

# Step 3: Create masks
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = mask1 + mask2

# Step 4: Invert mask
inverse_mask = cv2.bitwise_not(mask)

# Step 5: Remove red region (keep background)
background_removed = cv2.bitwise_and(img, img, mask=inverse_mask)

# Convert for display
background_removed_rgb = cv2.cvtColor(background_removed, cv2.COLOR_BGR2RGB)

plt.imshow(background_removed_rgb)
plt.title("Background Removed")
plt.axis("off")
plt.show()
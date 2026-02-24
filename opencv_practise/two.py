import cv2
import matplotlib.pyplot as plt

# 1️⃣ Load image
img = cv2.imread("data/image.jpeg")

# 2️⃣ Check if loaded
if img is None:
    print("Image not found")
    exit()

# 3️⃣ Copy image
img_copy = img.copy()

# 4️⃣ Now modify it
cv2.rectangle(img_copy, (50,50), (200,200), (0,255,0), 3)

# 5️⃣ Convert to RGB for display
img_rgb = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)

# 6️⃣ Show
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

data = []
labels = []

# Load dataset
for label, folder in enumerate(["cat", "dog"]):
    path = os.path.join("data", folder)
    
    for file in os.listdir(path):
        img_path = os.path.join(path, file)
        
        img = cv2.imread(img_path)
        if img is None:
            continue
        
        img = cv2.resize(img, (64, 64))  # FIXED SIZE
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        data.append(gray.flatten())  # convert to 1D
        labels.append(label)

# Convert to numpy
data = np.array(data)
labels = np.array(labels)

# Split data
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)


# Train model
model = SVC()
model.fit(X_train, y_train)
test_img = cv2.imread("data/cat/cat.jpeg")

if test_img is None:
    print("Error loading test image")
    exit()

test_img = cv2.resize(test_img, (64, 64))
gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

test_data = gray.flatten().reshape(1, -1)

# IMPORTANT: normalize same as training
test_data = test_data / 255.0

prediction = model.predict(test_data)

if prediction[0] == 0:
    print("Prediction: CAT 🐱")
else:
    print("Prediction: DOG 🐶")

# Test accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
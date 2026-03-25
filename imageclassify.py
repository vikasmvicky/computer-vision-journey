import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
data=[]
labels=[]

dataset_path="data"
 
for category in ["cat","dog"]:
    path=os.path.join(dataset_path,category)

    for img in os.listdir("data"):
        img_path=os.path.join(path,img)

        image=cv2.imread(img_path)
        image=cv2.resize(image,(64,64))

        data.append(image.flatten())
        labels.append(category)

        data=np.array(data)
        labels=np.array(labels)

        x_train,x_test,y_train,y_test=train_test_split(data,labels,test_size=0.2)

        model=SVC()
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)

        print("accuracy:",accuracy_score(y_pred))

import numpy as np
import numpy as np
import cv2
import os
import random
from matplotlib import pyplot as plt #import as plt so we can use it later
import pickle

DIRECTORY = #WRITE DIRECTORY
CATEGORIES = #DIFFERENT TYPES OF GROCERIES

IMG_SIZE = 100

data = []

for category in CATEGORIES:
    #matches image folders
    folder = os.path.join(DIRECTORY, category)

    label = CATEGORIES.index(category) #label image
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img) #finds image paths

        img_arr = cv2.imread(img_path)
        img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
        #img_arr = cv2.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
        #reshape may come in handy if we wish to work in grayscale

        #now we build data set
        data.append([img_arr, label]) #passes an image array with corresponding label

X = [] #X data set will store all features
y = [] #y will store all labels

for features, labels in data:
    X.append(features)
    y.append(labels)

#create numpy arrays
X = np.array(X)
y = np.array(y)

pickle.dump(X, open('X.pkl', 'wb'))
pickle.dump(y, open('y.pkl', 'wb'))

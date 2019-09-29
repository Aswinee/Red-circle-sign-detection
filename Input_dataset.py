import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
import math

# To store batches of data
X_mini_batches = []

# Paths to train and test folders
train_folder = os.path.join("F:\FullIJCNN2013", "Train")
test_folder = os.path.join("F:\FullIJCNN2013", "Test")

#Path of individual images
image_paths = os.listdir(train_folder)
train_img_num = (len(image_paths))

image_paths1 = os.listdir(test_folder)
test_img_num = (len(image_paths1))

desired_image_dim = 416

# Final train dataset of shape (600, 416, 416, 3) and test dataset of shape (300, 416, 416, 3)
X_train = np.ndarray(shape=(train_img_num, desired_image_dim, desired_image_dim, 3), dtype=np.float16)
X_test = np.ndarray(shape=(test_img_num, desired_image_dim, desired_image_dim, 3), dtype=np.float16)

#Pre-processing of train images
num_images = 0
for image in image_paths:
    image_path = os.path.join(train_folder, image)
    image_data = plt.imread(image_path).astype(float)                                                           # read image
    image_gray = np.dot(image_data, [0.2989, 0.5870, 0.1140])
    image_norm = (image_data - 255/2)/255                                                                       # normalise
    image_small = cv2.resize(image_norm, (desired_image_dim, desired_image_dim), interpolation = cv2.INTER_AREA)# resize
    X_train[num_images, :, :, :] = image_small                                                                  # assign
    num_images += 1

#Pre-processing of test images
numimage = 0
for image in image_paths1:
    image_path = os.path.join(test_folder, image)
    image_data = plt.imread(image_path).astype(float)                                                           #read image
    image_gray = np.dot(image_data, [0.2989, 0.5870, 0.1140])
    image_norm = (image_data - 255/2)/255                                                                       #normalize
    image_small = cv2.resize(image_norm, (desired_image_dim, desired_image_dim), interpolation = cv2.INTER_AREA)#resize
    X_test[numimage, :, :, :] = image_small                                                                     #assign
    numimage += 1

X_train = X_train[0:num_images, :, :, :]
print("Full train data shape : ", X_train.shape)

X_test = X_test[0:numimage, :, :, :]
print("Full test data shape : ", X_test.shape)

# Train data as Mini - batches

mini_batch_size = 32
num_minibatch = math.floor(train_img_num / mini_batch_size)
for k in range(0, num_minibatch):
    mini_batch_Xtrain = X_train[k*mini_batch_size :(k+1)*mini_batch_size - 1, :, :, :]
    X_mini_batches.append(mini_batch_Xtrain)

mini_batch_Xtrain = X_train[num_minibatch*mini_batch_size:599, :, :, :]
X_mini_batches.append(mini_batch_Xtrain)

print("Mean of X_train", np.mean(X_train))
print("Mean of X_test", np.mean(X_test))

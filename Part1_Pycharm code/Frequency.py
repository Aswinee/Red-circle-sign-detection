#Returns frequency of first 600 images from each class
import os
import numpy as np
import csv

Y_train = np.ndarray(shape=(600, 4), dtype=np.float16)
frequency = np.zeros((43, 0))
arr = []
for i in range(43):
    arr.append(0)
with open("gt.txt", newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    line_count = 0
    ind =0
    for row in csv_reader:

        if line_count <= 599:
            ind = int(row[5])
            frequency[ind] += 1
            arr[ind] += 1
            line_count += 1

    print("Frequency of images from each class:", arr)
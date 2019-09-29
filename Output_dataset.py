import numpy as np
import csv

Y_train = []
Y_test = []

# Read the annotation file
with open("gt.txt", newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # Appending the image name and ROI of first 600 images
        if line_count <= 851:

            Y_train.append([row[0], row[1], row[2], row[3], row[4]])
            line_count += 1

        # Appending the image name and ROI of remaining images
        elif line_count <= 1213:

            Y_test.append([row[0], row[1], row[2], row[3], row[4]])
            line_count += 1

    print("Y_train : ", Y_train)
    print("Y_Test : ", Y_test)
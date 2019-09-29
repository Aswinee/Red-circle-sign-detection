1.Description:

This is ReadMe.txt for execution of part 1 of the Detection of Red circled signs practice questions.

2.Data :

The whole data is shared using Dropbox. The shared Dropbox FulllJCNN2013 folder consists of

a. Test - 300 images used for testing 00600.ppm - 00899.ppm
b. Train - 600 images used for training 00000.ppm - 00599.ppm
c. a text file gt.txt containing the ground truth for all traffic signs in the images

3.Code:

a.Input_dataset.py:  Outputs X_train and X_test after preprocessing. Also outputs mean of both sets.
 Execution :         1. Download FulllJCNN2013 folder from dropbox and save it locally in a drive
                     2. Give the datapath of Train and Test folder to the os.path commands and run it.

b.Output_dataset.py: Outputs Y_train and Y_test from ground text file. 
 Execution :         1. Download FulllJCNN2013 folder from dropbox and save it locally in a drive
                     2. Give the datapath gt.txt file in the code and run it.

c.frequency.py:      Outputs frequency of images in each class. 
 Execution :         1. Download FulllJCNN2013 folder from dropbox and save it locally in a drive
                     2. Give the datapath gt.txt file in the code and run it.

4. Explanation of ground truth text file

The text file contains a line of the form
#ImgNo#.ppm;#leftCol#;##topRow#;#rightCol#;#bottomRow#;#ClassID#
for each traffic sign in the dataset. The first field refers to the image file the traffic sign is located in. Field 2 to 5 describe
the region of interest (ROI) in that image. Finally, the ClassID is an integer number representing the kind of traffic sign. 
The mapping is as follows:

0 = speed limit 20 (prohibitory)
1 = speed limit 30 (prohibitory)
2 = speed limit 50 (prohibitory)
3 = speed limit 60 (prohibitory)
4 = speed limit 70 (prohibitory)
5 = speed limit 80 (prohibitory)
6 = restriction ends 80 (other)
7 = speed limit 100 (prohibitory)
8 = speed limit 120 (prohibitory)
9 = no overtaking (prohibitory)
10 = no overtaking (trucks) (prohibitory)
11 = priority at next intersection (danger)
12 = priority road (other)
13 = give way (other)
14 = stop (other)
15 = no traffic both ways (prohibitory)
16 = no trucks (prohibitory)
17 = no entry (other)
18 = danger (danger)
19 = bend left (danger)
20 = bend right (danger)
21 = bend (danger)
22 = uneven road (danger)
23 = slippery road (danger)
24 = road narrows (danger)
25 = construction (danger)
26 = traffic signal (danger)
27 = pedestrian crossing (danger)
28 = school crossing (danger)
29 = cycles crossing (danger)
30 = snow (danger)
31 = animals (danger)
32 = restriction ends (other)
33 = go right (mandatory)
34 = go left (mandatory)
35 = go straight (mandatory)
36 = go right or straight (mandatory)
37 = go left or straight (mandatory)
38 = keep right (mandatory)
39 = keep left (mandatory)
40 = roundabout (mandatory)
41 = restriction ends (overtaking) (other)
42 = restriction ends (overtaking (trucks)) (other)
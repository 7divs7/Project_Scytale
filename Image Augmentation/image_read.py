import cv2
import numpy as np

img = cv2.imread('test.png')
rows, cols, channels = img.shape

for i in range (0,rows):
    for j in range (0,cols):
        print(img[i][j][0],end = " ")
    print('\n')
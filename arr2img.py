import numpy as np
import cv2

b = np.ones([300,300,1])

a = np.zeros([300,300,1])

cv2.imshow('image1', a)
cv2.imshow('image2', b)

cv2.waitKey(0)
cv2.destroyAllWindows()
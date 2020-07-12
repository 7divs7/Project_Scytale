import cv2
import numpy as np

img = cv2.imread('test.png')
rows, cols, channels = img.shape
bigger = cv2.resize(img, (256, 256)) 
cv2.imshow('window',bigger)

cv2.waitKey()
cv2.destroyAllWindows()

# import h5py
# filename = ".h5"

# with h5py.File(filename, "r") as f:
#     # List all groups
#     print("Keys: %s" % f.keys())
#     a_group_key = list(f.keys())[0]

#     # Get the data
#     data = list(f[a_group_key])
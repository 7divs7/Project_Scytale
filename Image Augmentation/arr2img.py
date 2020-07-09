import numpy as np
import matplotlib.pyplot as plt 

grid = [[0, 1, 1, 1, 1, 0, 0, 1], 
        [0, 1, 1, 1, 1, 1, 1, 1], 
        [0, 1, 0, 0, 0, 0, 1, 0], 
        [1, 1, 1, 0, 1, 1, 0, 0], 
        [0, 0, 0, 1, 1, 1, 0, 0], 
        [1, 0, 1, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 1, 1, 0], 
        [1, 0, 0, 0, 1, 0, 0, 1]]

x = np.asarray(grid)
print(x.shape)
plt.imshow(x, cmap='gray')
plt.show()

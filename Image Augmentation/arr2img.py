import numpy as np
import random
from PIL import Image
import h5py

def generate():
        grid = []
        for i in range(8):
                grid.append(random.randint(0,255))
        return grid

def main():
        imgarr = []
        n = int(input('Enter Number of Data Chunks: '))
        temp = n
        while n!=0:
                line_matrix = generate()
                grid = []
                for i in range (0,8):
                        grid.append(line_matrix)
                grid = np.array(grid)
                img = Image.fromarray(np.uint8(grid))
                imgarr.append(img)
                n -= 1

        file = h5py.File("storage.h5","w")
        dataset = file.create_dataset("images", np.shape(imgarr), h5py.h5t.STD_U8BE, data = imgarr)
        file.close()

        # img.save('test.png')

if __name__ == "__main__":
        main()
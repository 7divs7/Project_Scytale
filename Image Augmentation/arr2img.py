import numpy as np
import random
from PIL import Image

def generate():
        grid = []
        for i in range(8):
                grid.append(random.randint(0,255))
        return grid

def main():
        n = int(input('Enter Number of Data Chunks: '))
        while n!=0:
                line_matrix = generate()
                grid = []
                for i in range (0,8):
                        grid.append(line_matrix)
                n -= 1
        grid = np.array(grid)
        # print(grid)
        img = Image.fromarray(np.uint8(grid))
        img.save('test.png')

if __name__ == "__main__":
        main()
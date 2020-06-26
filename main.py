grid = [[0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]]

'''
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 1, 1, 1],

'''


def right_shift(seq, n=1):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def split_4_pair(row):
    temp = []
    for i in range(0,len(row),2):
        temp.append((row[i],row[i+1]))
    return temp


def form_blue_grid(grid):
    blue_grid = []
    for i in range(0,len(grid),2):
        t = split_4_pair(grid[i])
        t_next = split_4_pair(grid[i+1])
        for i in range(len(t)):
            dec = t[i][0]*8+t[i][1]*4+t_next[i][0]*2+t_next[i][1]
            blue_grid.append(dec)
    blue = []
    for i in range(0,len(blue_grid),4):
        blue.append(blue_grid[i:i+4])
    return blue

def form_red_grid(grid):
    last_row = grid[len(grid)-1]
    # print(last_row)

    red_grid = []
    for row in grid:
        red_grid.append(right_shift(row))

    red_grid.insert(0,last_row)
    red_grid.pop(len(grid))

    red_grid = form_blue_grid(red_grid)
    return red_grid

blue_grid = form_blue_grid(grid)
# print(blue_grid)


red_grid = form_red_grid(grid)
# print(red_grid)

def convert_blue_decimalNeighbourhood_to_grid(blue_grid):
    grid = []
    for row in blue_grid:
        odd_row = []
        even_row = []
        for i in row:
            b = [int(j) for j in list('{0:0b}'.format(i))]
            while(len(b)<4):
                b.insert(0,0)
            odd_row.append(b[0])
            odd_row.append(b[1])
            even_row.append(b[2])
            even_row.append(b[3])
        grid.append(odd_row)
        grid.append(even_row)
    return grid

# print(convert_blue_decimalNeighbourhood_to_grid(red_grid))
            

def convert_red_decimalNeighbourhood_to_grid(red_grid):
    '''
    pop first row
    insert first row at the end append
    left shift by 1
    '''
    temp = convert_blue_decimalNeighbourhood_to_grid(red_grid)
    t = temp[0]
    temp.pop(0)
    temp.append(t)
    grid = []
    for row in temp:
        grid.append(right_shift(row,7))
    return grid

print(convert_red_decimalNeighbourhood_to_grid(red_grid))
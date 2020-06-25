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
    return blue_grid

def form_red_grid(grid):
    last_row = grid[len(grid)-1]
    # print(last_row)

    transpose_grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))] 
    last_col = transpose_grid[len(transpose_grid)-1]
    # print(last_col)

    red_grid = []
    for row in grid:
        red_grid.append(right_shift(row))

    red_grid.insert(0,last_row)
    red_grid.pop(len(grid))

    red_grid = form_blue_grid(red_grid)
    return red_grid

print(form_blue_grid(grid))
print(form_red_grid(grid))
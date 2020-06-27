grid = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 1, 1]]

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
print('\n')
print(blue_grid)


# red_grid = form_red_grid(grid)
# print(red_grid)

def forward_transformation(blue_grid):
    final_transformed_blue_grid = []
    for row in blue_grid:
        transformed_blue_grid = []
        for i in row:
            if i == 0:
                transformed_blue_grid.append(15)
            elif i == 1:
                transformed_blue_grid.append(14)
            elif i == 2:
                transformed_blue_grid.append(13)
            elif i == 3:
                transformed_blue_grid.append(3)
            elif i == 4:
                transformed_blue_grid.append(11)
            elif i == 5:
                transformed_blue_grid.append(5)
            elif i == 6:
                transformed_blue_grid.append(6)
            elif i == 7:
                transformed_blue_grid.append(1)
            elif i == 8:
                transformed_blue_grid.append(7)
            elif i == 9:
                transformed_blue_grid.append(9)
            elif i == 10:
                transformed_blue_grid.append(10)
            elif i == 11:
                transformed_blue_grid.append(2)
            elif i == 12:
                transformed_blue_grid.append(12)
            elif i == 13:
                transformed_blue_grid.append(4)
            elif i == 14:
                transformed_blue_grid.append(8)
            elif i == 15:
                transformed_blue_grid.append(0)
        final_transformed_blue_grid.append(transformed_blue_grid)
    return final_transformed_blue_grid

print('\n')
print(forward_transformation(blue_grid))

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
tr_grid = convert_blue_decimalNeighbourhood_to_grid(forward_transformation(blue_grid))
print(tr_grid)



# print(convert_blue_decimalNeighbourhood_to_grid([[15,14,13,3],
# [11,5,6,1],
# [7,9,10,2],
# [12,4,8,0]]))

print('\n')
print(form_red_grid(tr_grid))


print('\n')
print(forward_transformation(form_red_grid(tr_grid)))



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

# print(convert_red_decimalNeighbourhood_to_grid(red_grid))



print('\n')
print(convert_red_decimalNeighbourhood_to_grid(forward_transformation(form_red_grid(tr_grid))))

def right_shift(seq, n=1):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]

def split_4_pair(row):
    temp = []
    for i in range(0,len(row),2):
        temp.append((row[i],row[i+1]))
    return temp

def evolve(grid,flag,enc_or_dec):
    if flag%2 == 0:
        # blue neighbourhood
        blue = []
        for i in range(0,len(grid),2):
            t = split_4_pair(grid[i])
            t_next = split_4_pair(grid[i+1])
            for i in range(len(t)):
                dec = t[i][0]*8+t[i][1]*4+t_next[i][0]*2+t_next[i][1]
                blue.append(dec)
        blue_neighbhourhood = []
        for i in range(0,len(blue),4):
            blue_neighbhourhood.append(blue[i:i+4])

        if enc_or_dec == 'encrypt':
            blue_neighbhourhood = forward_transformation(blue_neighbhourhood)
        else:
            blue_neighbhourhood = reverse_transformation(blue_neighbhourhood)

        evolved_grid = []
        for row in blue_neighbhourhood:
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
            evolved_grid.append(odd_row)
            evolved_grid.append(even_row)
        return evolved_grid

    else:
        # red neighbourhood
        
        temp_red_neighbourhood = []
        for row in grid:
            temp_red_neighbourhood.append(right_shift(row))

        last_row = temp_red_neighbourhood[len(temp_red_neighbourhood)-1]
        
        temp_red_neighbourhood.insert(0,last_row)
        temp_red_neighbourhood.pop(len(temp_red_neighbourhood)-1)

        red = []
        for i in range(0,len(temp_red_neighbourhood),2):
            t = split_4_pair(temp_red_neighbourhood[i])
            t_next = split_4_pair(temp_red_neighbourhood[i+1])
            for i in range(len(t)):
                dec = t[i][0]*8+t[i][1]*4+t_next[i][0]*2+t_next[i][1]
                red.append(dec)
        red_neighbhourhood = []
        for i in range(0,len(red),4):
            red_neighbhourhood.append(red[i:i+4])
        
        if enc_or_dec == 'encrypt':
            red_neighbhourhood = forward_transformation(red_neighbhourhood)
        else:
            red_neighbhourhood = reverse_transformation(red_neighbhourhood)

        # print(red_neighbhourhood)

        temp = []
        for row in red_neighbhourhood:
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
            temp.append(odd_row)
            temp.append(even_row)
        
        t = temp[0]
        temp.pop(0)
        temp.append(t)
        evolved_grid = []
        for row in temp:
            evolved_grid.append(right_shift(row,7))
        return evolved_grid
        

def forward_transformation(neighbourhood):
    new_neighbourhood = []
    for row in neighbourhood:
        temp = []
        for i in row:
            if i == 0:
                temp.append(15)
            elif i == 1:
                temp.append(14)
            elif i == 2:
                temp.append(13)
            elif i == 3:
                temp.append(3)
            elif i == 4:
                temp.append(11)
            elif i == 5:
                temp.append(5)
            elif i == 6:
                temp.append(6)
            elif i == 7:
                temp.append(1)
            elif i == 8:
                temp.append(7)
            elif i == 9:
                temp.append(9)
            elif i == 10:
                temp.append(10)
            elif i == 11:
                temp.append(2)
            elif i == 12:
                temp.append(12)
            elif i == 13:
                temp.append(4)
            elif i == 14:
                temp.append(8)
            elif i == 15:
                temp.append(0)
        new_neighbourhood.append(temp)
    return new_neighbourhood

def reverse_transformation(neighbourhood):
    new_neighbourhood = []
    for row in neighbourhood:
        temp = []
        for i in row:
            if i == 0:
                temp.append(15)
            elif i == 1:
                temp.append(7)
            elif i == 2:
                temp.append(11)
            elif i == 3:
                temp.append(3)
            elif i == 4:
                temp.append(13)
            elif i == 5:
                temp.append(5)
            elif i == 6:
                temp.append(6)
            elif i == 7:
                temp.append(8)
            elif i == 8:
                temp.append(14)
            elif i == 9:
                temp.append(9)
            elif i == 10:
                temp.append(10)
            elif i == 11:
                temp.append(4)
            elif i == 12:
                temp.append(12)
            elif i == 13:
                temp.append(2)
            elif i == 14:
                temp.append(1)
            elif i == 15:
                temp.append(0)
        new_neighbourhood.append(temp)
    return new_neighbourhood

def padding(plain_text,block_size):
    plain_text += '0'*(block_size-len(plain_text))
    return plain_text

def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))

def dec_to_bin_list(dec):
    b = [int(i) for i in list('{0:0b}'.format(dec))]
    while len(b)<8:
        b.insert(0,0)
    return b

def bin_list_to_dec(binary_list):
    return int("".join(str(x) for x in binary_list), 2)

def encrypt(plaintext,blocksize=8,iterations=10):
    chunks =  chunkstring(plaintext,blocksize)
    chunks[-1] = padding(chunks[-1],blocksize)
    # print(chunks)
    binary_ascii_chunks = []
    for chunk in chunks:
        temp = []
        for character in chunk:
            temp.append(dec_to_bin_list(ord(character)))
        binary_ascii_chunks.append(temp)
    # print(binary_ascii_chunks)
    encrypted_grids = []
    for binary_grid in binary_ascii_chunks:
        for i in range(iterations):
            new_grid = evolve(binary_grid,flag=i,enc_or_dec='encrypt')
            binary_grid = new_grid
        encrypted_grids.append(binary_grid)

    ciphertext = []
    for encrypted_binary_grid in encrypted_grids:
        temp = []
        for row in encrypted_binary_grid:
            ascii_val = bin_list_to_dec(row)
            temp.append(ascii_val)
        # print('----------------')
        ciphertext.append(temp)
    # print(ciphertext)
    return ciphertext
   
def decrypt(ciphertext,iterations=10,blocksize=8):
    binary_encrypted_grids = []
    for chunk in ciphertext:
        temp = []
        for num in chunk:
            temp.append(dec_to_bin_list(num))
        binary_encrypted_grids.append(temp)

    ascii_values = []
    for binary_grid in binary_encrypted_grids:
        for i in range(1,iterations+1):
            new_grid = evolve(binary_grid,flag=i,enc_or_dec='decrypt')
            binary_grid = new_grid

        for row in binary_grid:
            ascii_values.append(bin_list_to_dec(row))

    for i in range(len(ascii_values)-1,0,-1):
        if ascii_values[i] == ord('0'):
            ascii_values.pop(i)

    decryptedtext = ''
    for num in ascii_values:
        decryptedtext += chr(num)
    
    return decryptedtext

# iterations = 52

# grid = [[0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0, 1, 1],
#         [0, 1, 0, 1, 0, 1, 0, 1],
#         [0, 0, 0, 1, 1, 0, 1, 1],
#         [1, 0, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 1, 1, 0, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 1, 1, 0, 1, 1]]


# ################################## ENCRYPTION ##################################
# print('Encrypting...')
# for i in range(iterations):
#     new_grid = evolve(grid,flag=i,enc_or_dec='encrypt')
#     grid = new_grid

# for row in grid:
#     print(row)

# ################################## DECRYPTION ##################################
# print('Decrypting...')
# for i in range(1,iterations+1):
#     new_grid = evolve(grid,flag=i,enc_or_dec='decrypt')
#     grid = new_grid

# for row in grid:
#     print(row)
import random
from critters import evolve
import pandas as pd


#print(random.choice([0,1]))
print("GENERTATE\n")

grid = []
for i in range(8):
    temp = []
    for j in range(8):
        temp.append(random.choice([0,1]))
    grid.append(temp)

for i in grid:
    print(i)

print()

tup = ()
data = []

################################## ENCRYPTION ##################################
#print('Encrypting...')
for i in range(50):
    if(i%2 == 0 and i!=0):
        data.append(tup)
        tup = (i,)
            
    new_grid = evolve(grid,flag=i,enc_or_dec='encrypt')
    grid = new_grid
    tup = tup + (grid,) 


for row in data:
    for col in row:
        print(col)
    print()

my_df = pd.DataFrame(data)
my_df.to_csv('/Users/divyani/Desktop/my_csv.csv', index=False, header=False)
    

   

    
from difflib import *
from critters import *

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == '__main__':

    blocksize = 8
    privatekey = int(input('Private key : '))

    plaintext1 = input('Secret Message 1 : ')
    plaintext2 = input('Secret Message 2 : ')

    ciphertext1 = encrypt(plaintext1,iterations=privatekey,blocksize=blocksize)
    ciphertext2 = encrypt(plaintext2,iterations=privatekey,blocksize=blocksize)
    
    print('Percentage similarity : ',end='')
    print(similar(ciphertext1[0],ciphertext2[0])*100)
 
    print('CipherText 1 : ',end='')
    print(ciphertext1)

    print('CipherText 2 : ',end='')
    print(ciphertext2)



from critters import *
import time




if __name__ == '__main__':

    blocksize = 8
    privatekey = int(input('Private key : '))

    plaintext = input('Secret Message : ')

    start = time.time()
    ciphertext = encrypt(plaintext,iterations=privatekey,blocksize=blocksize)
    decryptedtext = decrypt(ciphertext,iterations=privatekey,blocksize=blocksize)
    end = time.time()

    print('CipherText : ',end='')
    print(ciphertext)
    print('Decrypted Text : ',end='')
    print(decryptedtext)

    print('Run Time : ' + str(end-start))    
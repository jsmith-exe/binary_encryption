# Jamie V Smith
# Decrypt File

import conversion as cnv

def read_key():
    with open("key.txt", 'r') as data:
        key = data.read().strip()
    
    return int(key)

def decrypt_bit(c, key):
    plaintext = (c % key) % 2 

    return plaintext

def decrypt_int(c):
    key = read_key()

    binArray = []
    for bit in c:
        dec_bit = decrypt_bit(bit, key)
        binArray.append(dec_bit)

    integer = cnv.binary_to_int(binArray)

    return integer

    

    


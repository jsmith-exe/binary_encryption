# Jamie V Smith
# Encrypt File

import os
import keyGenerator as key_gen
import variable as v
import conversion as cnv

def save_ciphertext(ciphertext):
    currentDir = os.path.dirname(os.path.abspath(__file__))
    encrypted_data_dir = os.path.join(currentDir, '..', 'encrypted_data')
    ciphertext_file_path = os.path.join(encrypted_data_dir, 'ciphertext.txt')

    with open(ciphertext_file_path, 'w') as file:
        file.write(str(ciphertext))

def encrypt_bit(m):
    key = key_gen.generate_key()
    r = v.generate_r()
    q = v.generate_large_random_int()
    c = m + (2 * r) + (key * q)
    
    return c

def encrypt_int(integer):
    binArray = cnv.int_to_binary(integer)

    key = key_gen.generate_key()
    encArray = []
    for m in binArray:
        r = v.generate_r()
        q = v.generate_large_random_int()
        
        c = m + (2 * r) + (key * q)
        encArray.append(c)

    save_ciphertext(encArray)

    return encArray





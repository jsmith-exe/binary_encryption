# Jamie V Smith
# Testing Decrypt

import os

def binary_to_int(binArray):
    bin_str = ''.join(map(str, binArray))
    integer = int(bin_str, 2)

    print(F"Restored Binary Value: {binArray}")

    return integer

def read_key():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    encrypted_data_dir = os.path.join(currentDir, '..', 'encrypted_data')
    key_file_path = os.path.join(encrypted_data_dir, 'key.txt')

    with open(key_file_path, 'r') as data:
        key = data.read().strip()
    
    return int(key)

def read_ciphertext():
    currentDir = os.path.dirname(os.path.abspath(__file__))
    encrypted_data_dir = os.path.join(currentDir, '..', 'encrypted_data')
    ciphertext_file_path = os.path.join(encrypted_data_dir, 'ciphertext.txt')

    with open(ciphertext_file_path, 'r') as data:
        ciphertext = data.read().strip()
    
    ciphertext = ciphertext.replace(",", "").replace("[", "").replace("]", "")
    
    return list(map(int, ciphertext.split()))

def decrypt_bit(c, key):
    plaintext = (c % key) % 2

    return plaintext

def decrypt_int():
    key = read_key()
    ciphertext = read_ciphertext()

    binArray = []
    for bit in ciphertext:
        dec_bit = decrypt_bit(bit, key)
        binArray.append(dec_bit)

    integer = binary_to_int(binArray)

    return integer
# Jamie V Smith
# Main Encrypt Test

import encrypt

if __name__ == '__main__':

    integer = int(input("Input Integer: "))
    ciphertext = encrypt.encrypt_int(integer)
    print ("Ciphertext & Key Saved")

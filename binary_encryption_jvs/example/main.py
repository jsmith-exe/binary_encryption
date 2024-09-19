# Jamie V Smith
# Main File

import encrypt
import decrypt
import check

if __name__ == '__main__':

    integer = int(input("Input Integer: "))
    ciphertext = encrypt.encrypt_int(integer)
    print (F'Ciphertext: {ciphertext}')

    integer_restored = decrypt.decrypt_int(ciphertext)
    print (F'Restored Integer: {integer_restored}')

    check.comapare_val(integer, integer_restored)


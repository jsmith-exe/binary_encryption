# Jamie V Smith
# Encrypt File

import keyGenerator as key_gen
import variable as v
import conversion as cnv

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

    return encArray





# Jamie V Smith
# Number Base Conversion File

def int_to_binary(integer):
    bin_string = bin(integer)[2:]

    binArray_str = []
    for i in bin_string:
        binArray_str.append(i)

    binArray = list(map(int, binArray_str))

    print (F"Input Binary Value: {binArray}")

    return binArray

def binary_to_int(binArray):
    bin_str = ''.join(map(str, binArray))
    integer = int(bin_str, 2)

    print(F"Restored Binary Value: {binArray}")

    return integer
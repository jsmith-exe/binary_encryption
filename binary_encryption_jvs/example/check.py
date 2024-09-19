# Jamie V Smith
# Checking File

def comapare_val(input, output):
    diff = (input - output)
    if (diff != 0):
        print (F"Difference in Values of : {diff}")

    if (diff == 0):
        print ("Succesfully Decrypted")
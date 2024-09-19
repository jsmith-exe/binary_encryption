# Jamie V Smith
# Key Generation File

import random

def save_key(key):
    with open(F'key.txt', 'w') as file:
        file.write(str(key))

def generate_key(num_digits=8):
    if num_digits < 1:
        raise ValueError("Number of digits must be at least 1.")

    # Ensure the first digit is not zero to avoid leading zeros
    first_digit = random.randint(1, 9)
    
    # Generate the remaining digits
    remaining_digits = [random.randint(0, 9) for _ in range(num_digits - 1)]
    
    # Combine all digits into a single integer
    random_key = int(str(first_digit) + ''.join(map(str, remaining_digits)))
    
    save_key(random_key)  # Assuming save_key is defined elsewhere to save the key
    
    return random_key



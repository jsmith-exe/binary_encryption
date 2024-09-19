# Jamie V Smith
# Variables File

import random

def generate_r(num_digits=3):
    if num_digits < 1:
        raise ValueError("Number of digits must be at least 1.")
    
    # Ensure the first digit is not zero
    first_digit = random.randint(1, 9)
    
    # Generate the rest of the digits
    remaining_digits = [random.randint(0, 9) for _ in range(num_digits - 1)]
    
    # Combine all digits into a single integer
    large_random_int = int(str(first_digit) + ''.join(map(str, remaining_digits)))
    
    return large_random_int

def generate_large_random_int(num_digits=3):
    if num_digits < 1:
        raise ValueError("Number of digits must be at least 1.")

    # Ensure the first digit is not zero to avoid leading zeros
    first_digit = random.randint(1, 9)
    
    # Generate the remaining digits
    remaining_digits = [random.randint(0, 9) for _ in range(num_digits - 1)]
    
    # Combine all digits into a single integer
    random_int = int(str(first_digit) + ''.join(map(str, remaining_digits)))
    
    if ((random_int % 2) != 0): 
        random_int += 1
    
    return random_int




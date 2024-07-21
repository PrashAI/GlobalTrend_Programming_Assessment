# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:50:15 2024

@author: prasa
"""

import random
import string

def generate_random_password(length=12):
    """
    Generate a random password containing uppercase letters, lowercase letters, digits, and special characters.

    Parameters:
    length (int): The length of the password to generate. Default is 12.

    Returns:
    str: The generated random password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to ensure diversity of character types.")
    
    # Define the character sets to use
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure at least one character from each set is included
    password = [
        random.choice(upper_case),
        random.choice(lower_case),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining length of the password with random choices from all character sets
    all_characters = upper_case + lower_case + digits + special_characters
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the list to ensure random distribution of character types
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Example usage:
password_length = 16
print(f"Generated password: {generate_random_password(password_length)}")

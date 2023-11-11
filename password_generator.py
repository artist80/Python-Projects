#!/usr/bin/env python3

import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, symbols=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    try:
        length = int(input("Enter password length: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'

        return length, uppercase, lowercase, numbers, symbols
    except ValueError:
        print("Error: Please enter a valid integer for password length.")
        return get_user_input()


if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    length, uppercase, lowercase, numbers, symbols = get_user_input()
    
    password = generate_password(length, uppercase, lowercase, numbers, symbols)
    
    print(f"Generated Password: {password}")

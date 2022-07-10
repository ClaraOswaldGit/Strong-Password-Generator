# -*- coding: utf-8 -*-
"""
Code inspired by Fahmida Yesmin's tutorial: https://linuxhint.com/python-password-generator/'
"""

import pyperclip
import random

# Set the character list for generating the password
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"


# Generate strong password of at least 12 charachter length. Prompt user to re-enter length if under 12 characters.
def passGen():
    # Take the length of the password from the user
    password_length = int(input('Enter the length of the password: '))
    while True: 
        ## Set the minimum password length to 12 characters
        if password_length <= 11:
            ### Under 12 characters error message
            print('Strong passwords must be at least 12 characters long.')
            ### Prompt user to enter a higher lenght
            passGen()
            break
        else:
            # Generate the password
            password = "".join(random.sample(characters, password_length))
            # Print the generated password
            print("Gernerated password: %s" %password)
            break

passGen()

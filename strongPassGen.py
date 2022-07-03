# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 22:25:30 2022

@author: othar
"""

import pyperclip
import random

# Set the character list for generating the password
characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]|/\?!@#$%^abcdefghijklmnopqrstuvwxyz"
# Take the length of the password from the user
password_length = int(input('Enter the length of the password: '))
# Generate the password
password = "".join(random.sample(characters, password_length))
# Print the generated password
print("Gernerated password: %s" %password)



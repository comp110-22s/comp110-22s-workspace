"""Fun password generator."""


import random

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+-=[]',./<>?:"


length = input("How long would you like your password to be? ")
length = int(length)

print("\nHere is your password:")

password: str = ""
for n in range(length):
    password += random.choice(chars)

print(password)
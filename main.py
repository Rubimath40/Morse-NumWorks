import ion
import mu
import time

import alphabet

def encrypt(message):
    message = message.upper()
    for old, new in alphabet.encrypt.items():
        message = message.replace(old, new)
    return message

def decrypt(message):
    message = message + " "
    for old, new in alphabet.decrypt:
        message = message.replace(old, new)
    return message



## Test section
menu = input("1. Encrypt to Morse\n2. Decrypt from Morse\nChoice? ")
message = input("What's your message? ")
if menu == "1":
    print(encrypt(message))
else:
    print(decrypt(message))


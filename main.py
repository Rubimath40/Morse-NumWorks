import ion
import mu
import time

import alphabet

def encrypt(message):
    message = message.upper()
    for old, new in alphabet.encrypt.items():
        message = message.replace(old, new)
    return message


## Test section
message = input("What's your message? ")
print(encrypt(message))

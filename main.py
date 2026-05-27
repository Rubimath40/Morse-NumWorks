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

def send(message):
    for i in message:
        if i == ".":
            mu.set_led((255,0,0))
            time.sleep(0.1)
        elif i == "_":
            mu.set_led((255,0,0))
            time.sleep(0.5)
        else:
            time.sleep(1)
        mu.set_led((0,0,0))



## Test section
menu = input("1. Encrypt to Morse\n2. Decrypt from Morse\nChoice? ")
message = input("What's your message? ")
if menu == "1":
    print(encrypt(message))
else:
    print(decrypt(message))


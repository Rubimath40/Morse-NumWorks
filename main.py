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

def send(message, timeUnit=0.2):
    for i in message:
        if i == ".":
            mu.set_led((255,0,0))
            time.sleep(timeUnit)
        elif i == "_":
            mu.set_led((255,0,0))
            time.sleep(timeUnit*3)
        else:
            time.sleep(timeUnit*3)
        mu.set_led((0,0,0))
        time.sleep(timeUnit)


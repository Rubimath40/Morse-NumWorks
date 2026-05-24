import ion
import mu
import time

import alphabet

def encrypt(message):
    for old, new in alphabet.encrypt.items():
        message = message.replace(old, new)

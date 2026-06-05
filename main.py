import ion
import mu
import time

import alphabet

def encrypt(message):
    message = message.upper()
    for old, new in alphabet.encrypt:
        message = message.replace(old, new)
    return message

def decrypt(message):
    message += " "
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

def recieve(timeUnit=0.2):
    message = ""
    isPressed = False
    startTime = 0
    lastRelease = None

    while not ion.keydown(ion.KEY_BACKSPACE):
        if ion.keydown(ion.KEY_OK) and not isPressed:
            if lastRelease != None:
                releaseTime = time.monotonic() - lastRelease
                if  releaseTime < timeUnit * 3:
                    pass
                elif    releaseTime < timeUnit * 7:
                    message += " "
                else:
                    message += "  "
            startTime = time.monotonic()
            isPressed = True

        if not ion.keydown(ion.KEY_OK) and isPressed:
            endTime = time.monotonic()
            clicDuration = endTime - startTime

            if clicDuration < timeUnit * 3:
                message += "."
            else:
                message += "_"

            lastRelease = endTime
            isPressed = False

    message += " "
    return message

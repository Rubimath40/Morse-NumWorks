import ion
import mu
import time
import kandinsky

import alphabet

def encrypt(message):
    message = message.upper()
    for old, new in alphabet.morse:
        message = message.replace(old, new)
    return message

def decrypt(message):
    message += " "
    for new, old in alphabet.morse:
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

def receive(timeUnit=0.2):
    message = ""
    isPressed = False
    startTime = 0
    lastRelease = None

    long = timeUnit * 3
    space = timeUnit * 7

    while not ion.keydown(ion.KEY_BACKSPACE):
        kandinsky.draw_string(message, 0, 0)
        if ion.keydown(ion.KEY_OK) and not isPressed:
            if lastRelease != None:
                releaseTime = time.monotonic() - lastRelease
                if releaseTime < long:
                    pass
                elif releaseTime < space:
                    message += " "
                else:
                    message += "  "
            startTime = time.monotonic()
            isPressed = True

        if not ion.keydown(ion.KEY_OK) and isPressed:
            endTime = time.monotonic()
            clicDuration = endTime - startTime

            if clicDuration < long:
                message += "."
            else:
                message += "_"

            lastRelease = endTime
            isPressed = False

    message += " "
    return message

def liveSend():
    while not ion.keydown(ion.KEY_BACKSPACE):
        if ion.keydown(ion.KEY_OK):
            mu.set_led((255,0,0))
        else:
            mu.set_led((0,0,0))


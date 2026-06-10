import ion
import mu
import time
import kandinsky

import alphabet
class encryptionService:
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

class messageService:
    def send(message, timeUnit=0.2):
        mu.fill((0,0,0))
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
        mu.fill((0,0,0))
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
        mu.fill((0,0,0))
        kandinsky.draw_string("Press [BACKSPACE] to end message", 0, 204)
        while not ion.keydown(ion.KEY_BACKSPACE):
            if ion.keydown(ion.KEY_OK):
                mu.set_led((255,0,0))
            else:
                mu.set_led((0,0,0))

def chooseMode(listChoices=["1. Send a message", "2. Receive a message"]):
    kandinsky.fill_rect(0,0,320,222,(0,0,0))
    kandinsky.draw_string("\n".join(listChoices), 0, 0)

    while True:
        if ion.keydown(ion.KEY_ONE):
            while ion.keydown(ion.KEY_ONE):
                pass
            selectedMode = 1
            break

        elif ion.keydown(ion.KEY_TWO):
            while ion.keydown(ion.KEY_TWO):
                pass
            selectedMode = 2
            break
    return selectedMode

def main():
    while True:
        mode = chooseMode()
        if mode == 2:
            morseMessage = messageService.receive()
            message = encryptionService.decrypt(morseMessage)
            mu.fill((0,0,0))
            kandinsky.draw_string("Press [SHIFT] to exit", 110, 204)
            kandinsky.draw_string("The message is:", 85, 0)
            kandinsky.draw_string(message, 0, 20)
            while not ion.keydown(ion.KEY_SHIFT):
                pass
        elif mode == 1:
            sendingMode = chooseMode(["1. Live send", "2. Specify a message"])

            if sendingMode == 1:
                messageService.liveSend()
            elif sendingMode == 2:
                message = input("What is your message?\n")
                morseMessage = encryptionService.encrypt(message)
                messageService.send(morseMessage)


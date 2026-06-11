import ion
import mu
import time
import kandinsky

import alphabet

black = (0,0,0)
white = (255,255,255)

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
    def send(message, timeUnit=0.3):
        mu.fill(black)
        for i in message:
            if i == ".":
                mu.set_led((255,0,0))
                time.sleep(timeUnit)
            elif i == "_":
                mu.set_led((255,0,0))
                time.sleep(timeUnit*3)
            else:
                time.sleep(timeUnit*3)
            mu.set_led(black)
            time.sleep(timeUnit)

    def receive(timeUnit=0.3):
        global endTime, startTime
        mu.fill(black)
        kandinsky.draw_string("Press [BACKSPACE] to end message", 0, 204, black, white)
        message = ""
        isPressed = False
        startTime = 0
        endTime = 0
        lastRelease = None

        long = timeUnit * 3
        space = timeUnit * 7

        while not ion.keydown(ion.KEY_BACKSPACE):
            kandinsky.draw_string(message, 0, 0, black, white)
            if ion.keydown(ion.KEY_OK) and not isPressed:
                kandinsky.fill_rect(0, 186, 20, 18, black)
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
            if isPressed == True:
                if time.monotonic() - startTime < long:
                    kandinsky.draw_string(".", 0, 186, black, white)
                else:
                    kandinsky.draw_string("_", 0, 186, black, white)

            if not ion.keydown(ion.KEY_OK) and isPressed:
                endTime = time.monotonic()
                clicDuration = endTime - startTime

                if clicDuration < long:
                    message += "."
                else:
                    message += "_"

                lastRelease = endTime
                isPressed = False
            if not isPressed:

                if time.monotonic() - endTime < long:
                    kandinsky.fill_rect(0, 186, 20, 18, black)
                elif time.monotonic() - endTime < space:
                    kandinsky.draw_string(" ", 0, 186, black, white)
                else:
                    kandinsky.draw_string("  ", 0, 186, black, white)

        message += " "
        return message

    def liveSend():
        mu.fill(black)
        kandinsky.draw_string("Press [BACKSPACE] to end message", 0, 204, black, white)
        while not ion.keydown(ion.KEY_BACKSPACE):
            if ion.keydown(ion.KEY_OK):
                mu.set_led((255,0,0))
            else:
                mu.set_led(black)

def chooseMode(listChoices=["1. Send a message", "2. Receive a message"]):
    kandinsky.fill_rect(0,0,320,222,black)
    kandinsky.draw_string("\n".join(listChoices), 0, 0, black, white)

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

def main(timeUnit=0.3):
    while True:
        mode = chooseMode()
        if mode == 2:
            morseMessage = messageService.receive(timeUnit)
            message = encryptionService.decrypt(morseMessage)
            mu.fill(black)
            kandinsky.draw_string("Press [SHIFT] to exit", 110, 204, black, white)
            kandinsky.draw_string("The message is:", 85, 0, black, white)
            kandinsky.draw_string(message, 0, 20, black, white)
            while not ion.keydown(ion.KEY_SHIFT):
                pass
        elif mode == 1:
            sendingMode = chooseMode(["1. Live send", "2. Specify a message"])

            if sendingMode == 1:
                messageService.liveSend()
            elif sendingMode == 2:
                message = input("What is your message?\n")
                morseMessage = encryptionService.encrypt(message)
                messageService.send(morseMessage, timeUnit)

main()

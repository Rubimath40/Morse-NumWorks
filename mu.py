"""
This script is used to avoid error on computer and if you are running something other than Mu on your NumWorks.
It replace many things used in mu by kandinsky
"""
import kandinsky

def set_led(color=(0,0,0)):
    kandinsky.fill_rect(15, 15, 290, 192, color)

def fill(color=(0,0,0)):
    kandinsky.fill_rect(0, 0, 320, 222, color)

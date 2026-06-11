"""
This script is used to avoid error on computer and if you are running something other than Mu on your NumWorks.
It replace many things used in mu by kandinsky
"""
import kandinsky

def set_led(color):
    kandinsky.fill_rect(20, 20, 280, 182, color)

def fill(color):
    kandinsky.fill_rect(0, 0, 320, 222, color)

#!/usr/bin/env python3

import sys
import platform
import pyautogui as pya
from pyautogui import Point
import pyperclip

IS_MAC = (platform.system() == 'Darwin')

def clip_write_words(write_text: str, mouse_start_pos: Point):
    pya.moveTo(mouse_start_pos)
    words = [i.strip() for i in write_text.strip().split(" ")]

    for w in words:
        pya.press('esc')
        pya.press('t')
        pya.click()

        pyperclip.copy(w)

        if IS_MAC:
            modkey = 'command'
        else:
            modkey = 'ctrl'

        with pya.hold(modkey):
            pya.press('v')

        pya.moveRel(50, 10)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        write_text = pyperclip.paste()
    elif len(sys.argv) == 2:
        write_text = sys.argv[1]
    else:
        print("0 or 1 arguments are expected.")
        sys.exit(2)

    mouse_pos = pya.position()

    clip_write_words(write_text, mouse_pos)

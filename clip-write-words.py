#!/usr/bin/env python3

import sys
import time
import platform
import pyautogui as pya
from pyautogui import Point
import pyperclip

IS_MAC = (platform.system() == 'Darwin')

def write_words(write_text: str, mouse_start_pos: Point):
    pya.moveTo(mouse_start_pos)
    pya.click()
    time.sleep(0.1)

    words = [i.strip() for i in write_text.strip().split(" ")]

    x, y = mouse_start_pos

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

        x += 50
        y += 20
        pya.moveTo(x, y)
        time.sleep(0.1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        write_text = pyperclip.paste()
    elif len(sys.argv) == 2:
        write_text = sys.argv[1]
    else:
        print("0 or 1 arguments are expected.")
        sys.exit(2)

    print(f"Text: {write_text}")
    wait_secs = 5
    while wait_secs > 0:
        print(f"In {wait_secs}...")
        time.sleep(1)
        wait_secs -= 1

    mouse_pos = pya.position()
    write_words(write_text, mouse_pos)

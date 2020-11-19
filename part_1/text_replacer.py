#text_replacer.py
from pynput.keyboard import Key, Listener
import pyautogui

replacements = {"myname": "Firstname Lastname",
                "mymail": "abc@def.com",
               }

def on_press(key):
    global typed_keys
    global listening
    key_str = str(key).replace('\'', '')

    if key_str == macro_starter:
        typed_keys = []
        listening = True

    if listening:
        if key_str.isalpha():
            typed_keys.append(key_str)

        if key == macro_ender:
            candidate_keyword = ""
            candidate_keyword = candidate_keyword.join(typed_keys)
            if candidate_keyword != "":
                if candidate_keyword in replacements.keys():
                    pyautogui.press('backspace', presses=len(candidate_keyword)+2)
                    pyautogui.typewrite(replacements[candidate_keyword])
                    listening = False


macro_starter = '#'
macro_ender = Key.space
listening = True
typed_keys = []

with Listener(on_press=on_press) as listener:
    listener.join()

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# 일반 문자 입력
'''
keyboard.type("Hello, World!")
'''

# 특수 키 입력
'''
keyboard.press(Key.enter)
keyboard.release(Key.enter)
'''

# 단축키 조합 (Ctrl+C)
with keyboard.pressed(Key.ctrl):
    keyboard.press('v')
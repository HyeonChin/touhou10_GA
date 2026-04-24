import time
import pydirectinput
import subprocess
import gamestate
import random
import window

keys = [
    'up',
    'down',
    'left',
    'right',
    'x',
    'z'
]

start_key_sequence = [
    'z',
    'z',
    'z',
    'z'
]

play_key_sequence = [
]

restart_key_sequence = [
    'z',
    'up',
    'up'
]

window_box = 0

# ==============================


def press_key(key):
    pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)


def run_sequence(key_sequence, delay):
    print("<매크로 시작>")
    
    for key in key_sequence:
        print(f"키 입력: {key}")
        press_key(key)

        if gamestate.isGameOver(window_box):
            print("게임 오버!")
            break

        time.sleep(delay)


    print("<매크로 종료>")


if __name__ == "__main__":
    # subprocess.run(['C:/Users/system2020/Documents/동방/thcrap/th10 (ko).exe'])
    # time.sleep(10)
    for i in range(0, 400):
        play_key_sequence.append(random.choice(keys))

    window_box = window.activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
    run_sequence(start_key_sequence, 0.5)
    run_sequence(play_key_sequence, 0)

# 게임오버 확인 함수 구현
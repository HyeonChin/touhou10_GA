import time
import pydirectinput
import subprocess
import random
import window

# th10 프로그램 실행 후 타이틀 화면 진입하여서 시작

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
    'z',
]

play_key_sequence = [
]

delay_between_keys = 0.5   # 키 사이 간격 (초) — 빠른 연속입력
window_box = 0

# ==============================


def press_key(key):
    pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)
    time.sleep(delay_between_keys)


def run_sequence(key_sequence):
    print("▶ 매크로 시작!")
    
    for key in key_sequence:
        print(f"{key}키 입력!!")
        press_key(key)

    print("✅ 매크로 완료!")


if __name__ == "__main__":
    # subprocess.run(['C:/Users/system2020/Documents/동방/thcrap/th10 (ko).exe'])
    # time.sleep(10)
    for i in range(0, 100):
        play_key_sequence.append(random.choice(keys))

    window.activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
    delay_between_keys = 0.5
    run_sequence(start_key_sequence)
    delay_between_keys = 0
    run_sequence(play_key_sequence)
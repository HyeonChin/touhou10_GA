import time
import pydirectinput
import subprocess
import gamestate
import random
import window
import copy
import numpy as np

keys = [
    'up',
    'down',
    'left',
    'right',
    'x',
    'z',
    'shift'
]

start_key_sequence = [
    'z',
    'z',
    'z',
    'z'
]

retry_key_sequence = [
    'z',
    'up',
    'up',
    'z'
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


def keyinput_sequence(key_sequence, delay):
    print("<매크로 시작>")
    
    for key in key_sequence:
        if key == 'none':
            time.sleep(delay)
            continue
        print(f"키 입력: {key}")
        press_key(key)

        time.sleep(delay)

    print("<매크로 종료>")

def play_sequence(key_sequence):
    window_box = window.activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
    print("<매크로 시작>")

    s = 0
    for key in key_sequence:
        begin = time.time()
        if gamestate.isGameOver(window_box):
            print("게임 오버!")
            break

        press_key(key)
        s += 1
        end = time.time()
        print(f"{s}번 키 입력: {key}")
        delay = 0.8 - (end - begin)

        time.sleep(delay)
        
    print("<매크로 종료>")


# subprocess.run(['C:/Users/system2020/Documents/동방/thcrap/th10 (ko).exe'])
# time.sleep(10)
solution_n = 20
sequence_length = 200
generation = 0

play_key_sequence = [[None] * sequence_length for _ in range(solution_n)]
fit = [None] * solution_n

window_box = window.activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
keyinput_sequence(start_key_sequence, 0.5)
# keyinput_sequence(retry_key_sequence, 0.2)

for i in range(solution_n):
    for j in range(sequence_length):
        play_key_sequence[i][j] = random.choice(keys)

time.sleep(1)

while True:
    print(f"세대: {generation}")

    f = open("./log/fitlog0.txt", 'a')
    f.write(f"[generation_{generation}]\n")
    f.close()
    # 솔루션 적합도 측정 및 기록
    
    log_text = ""
    for i in range(solution_n):
        print(f"솔루션: {i}")

        begin = time.time()

        play_sequence(play_key_sequence[i])

        end = time.time()
        result = end - begin
        print(f"생존 시간: {result} 초")
        fit[i] = (result)

        log_text = f"soultion_{i}(fit={fit[i]}) : "
        for j in range(sequence_length):
            log_text += play_key_sequence[i][j] + "-"
        log_text += ";\n"

        f = open("./log/fitlog0.txt", 'a')
        f.write(log_text)
        f.close
        
        time.sleep(2)
        keyinput_sequence(retry_key_sequence, 1)

    # 솔루션 선택
    
    best_idx = fit.index(max(fit))
    play_key_sequence[0] = copy.deepcopy(play_key_sequence[best_idx])

    # 변이
    for i in range(1, solution_n):
        start_idx = 0
        end_idx = 0
        idx1 = random.randint(0, sequence_length)
        idx2 = random.randint(0, sequence_length)
        
        start_idx = min(idx1, idx2)
        end_idx = max(idx1, idx2)

        for j in range(start_idx, end_idx):
            play_key_sequence[i][j] = (random.choice(keys))

    generation += 1


# 게임오버 확인 함수 구현
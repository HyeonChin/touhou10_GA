import time
import pydirectinput
import subprocess
import gamestate
import random
import window
import copy
import numpy as np
import re

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
        delay = max(0, delay)
        time.sleep(delay)
        
    print("<매크로 종료>")
   



def load_from_log(filepath, solution_n, sequence_length):
    """로그 파일에서 마지막 세대 복원"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("로그 파일 없음. 새로 시작합니다.")
        return None, None, 0

    # 마지막 세대 번호 추출
    generations = re.findall(r'\[generation_(\d+)\]', content)
    if not generations:
        return None, None, 0
    
    last_gen = int(generations[-1])

    # 마지막 세대 블록 추출
    pattern = rf'\[generation_{last_gen}\](.*?)(?=\[generation_|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return None, None, 0

    block = match.group(1)

    # 각 솔루션 파싱
    solution_pattern = r'soultion_(\d+)\(fit=([\d.]+)\) : ([\w\-]+);'
    matches = re.findall(solution_pattern, block)

    if not matches:
        return None, None, 0

    play_key_sequence = [[None] * sequence_length for _ in range(solution_n)]
    fit = [0.0] * solution_n

    for m in matches:
        idx = int(m[0])
        fit_val = float(m[1])
        keys_str = m[2].strip('-').split('-')

        if idx < solution_n:
            fit[idx] = fit_val
            for j, k in enumerate(keys_str):
                if j < sequence_length:
                    play_key_sequence[idx][j] = k

    print(f"세대 {last_gen} 복원 완료. 솔루션 {len(matches)}개 로드.")
    return play_key_sequence, fit, last_gen, len(matches)

# subprocess.run(['C:/Users/system2020/Documents/동방/thcrap/th10 (ko).exe'])
# time.sleep(10)
solution_n = 20
sequence_length = 200

loaded_seq, loaded_fit, generation, solution = load_from_log("./log/fitlog0.txt", solution_n, sequence_length)

if loaded_seq is None:
    # 새로 시작
    play_key_sequence = [[None] * sequence_length for _ in range(solution_n)]
    fit = [0.0] * solution_n
    generation = 0
    solution = 0
    for i in range(solution_n):
        for j in range(sequence_length):
            play_key_sequence[i][j] = random.choice(keys)
    print("새로 시작합니다.")
else:
    # 이어서 시작 — 선택/변이 한 번 적용 후 재개
    play_key_sequence = loaded_seq
    fit = loaded_fit
    print(f"세대 {generation}부터 이어서 시작합니다.")

window_box = window.activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
keyinput_sequence(start_key_sequence, 0.5)
# keyinput_sequence(retry_key_sequence, 0.2)

for i in range(solution_n):
    for j in range(sequence_length):
        play_key_sequence[i][j] = random.choice(keys)

time.sleep(1)

while True:
    print(f"세대: {generation}")

    f = open("./log/fitlog1.txt", 'a')
    f.write(f"[generation_{generation}]\n")
    f.close()
    # 솔루션 적합도 측정 및 기록
    
    log_text = ""
    for i in range(solution, solution_n):
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

    # 솔루션 선택(순위 기반 선택)
    
    select_n = int(solution_n / 4)
    sorted_fit = sorted(fit, reverse=True)

    next_play_key_sequence = [None] * solution_n
    for i in range(0, solution_n):
        next_play_key_sequence[i] = copy.deepcopy(play_key_sequence[fit.index(sorted_fit[i % select_n])])
    play_key_sequence = next_play_key_sequence

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

 
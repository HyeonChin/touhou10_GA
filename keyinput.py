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
    'z',
    'shift',
    'none'
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

play_key_sequence = [[]]
fit = []

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

        if key == 'none':
            time.sleep(delay)
            continue
        press_key(key)
        s += 1
        end = time.time()
        print(f"{s}번 키 입력: {key}")
        delay = 0.8 - (begin - end)

        time.sleep(delay)
        
    print("<매크로 종료>")


if __name__ == "__main__":
    # subprocess.run(['C:/Users/system2020/Documents/동방/thcrap/th10 (ko).exe'])
    # time.sleep(10)
    solution_n = 100
    sequence_length = 200

    window_box = window.activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
    keyinput_sequence(start_key_sequence, 0.5)
    # keyinput_sequence(retry_key_sequence, 0.2)
    f = open("fitlog.txt", 'a')

    time.sleep(1)
    play_key_sequence = [[]]
    for i in range(solution_n):
        play_key_sequence.append([])
        begin = time.time()

        for _ in range(sequence_length):
            play_key_sequence[i].append(random.choice(keys))
        play_sequence(play_key_sequence[i])

        end = time.time()
        result = end - begin
        print(f"생존 시간: {result} 초")
        fit.append(result)

        text = f"soultion_{i}(fit={fit[i]}) : "
        for j in range(sequence_length):
            text += play_key_sequence[i][j] + "-"
        f.write(text + ";\n")
        
        time.sleep(2)
        keyinput_sequence(retry_key_sequence, 1)

    f.close



# 게임오버 확인 함수 구현
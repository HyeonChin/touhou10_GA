import time
import pyautogui
import pydirectinput
import subprocess


KEY_SEQUENCE = [
    'z',
    'z',
    'z',
    'z',
    'z',
]

delay_between_keys = 0.5   # 키 사이 간격 (초) — 빠른 연속입력
REPEAT_COUNT = 1             # 시퀀스 반복 횟수 (0 = 무한반복)
START_DELAY = 1              # 시작 전 대기 시간 (창 전환용)
window_box = 0

# ==============================


def activate_window(title):
    global window_box

    windows = pyautogui.getWindowsWithTitle(title)
    if windows:
        windows[0].activate()
        window_box = windows[0].left, windows[0].top, windows[0].width, windows[0].height
        print(f"'{title}' 창 있음")
    else:
        print(f"'{title}' 창 없음")

def press_key(key):
    pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)
    time.sleep(delay_between_keys)


def run_sequence():
    print(f"{START_DELAY}초 후 매크로 시작... (지금 게임 창으로 전환하세요!)")
    time.sleep(START_DELAY)
    print("▶ 매크로 시작!")

    if REPEAT_COUNT == 0:
        # 무한 반복
        count = 0
        while True:
            count += 1
            print(f"  [{count}번째 시퀀스]")
            for key in KEY_SEQUENCE:
                press_key(key)
    else:
        for i in range(REPEAT_COUNT):
            print(f"  [{i+1}/{REPEAT_COUNT}번째 시퀀스]")
            for key in KEY_SEQUENCE:
                print(f"{key}키 입력!!")
                press_key(key)

    print("✅ 매크로 완료!")


if __name__ == "__main__":
    # subprocess.run(['C:/Users/system2020/Documents/동방/thcrap/th10 (ko).exe'])
    # time.sleep(10)
    activate_window("동방풍신록 ~ Mountain of Faith. v1.00a")
    run_sequence()
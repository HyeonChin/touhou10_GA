import time
#import pyDirectInput
import keyboard

# FPS 및 프레임 시간 설정
frame_time = 0.1

# 'gaming' 상태 (0: 대기, 1: 기록 중)
gaming = 0

# Enter 키 입력 시 gaming 값 토글
def toggle_gaming():
    global gaming
    gaming = 1 - gaming
    if gaming == 1:
        print("keyDown started!")
    else:
        print("keyDown stopped!")

keyboard.add_hotkey("enter", toggle_gaming)

print("Press 'Enter' to start/stop recording...")

# 키 입력 함수
def press_key():
    pyDirectInput.press(pyDirectInput.KEY_UP)  # 위쪽 화살표 키 누르기

def release_key():
    pyDirectInput.release(pyDirectInput.KEY_UP)  # 위쪽 화살표 키 떼기

# 메인 루프

while True:
    if gaming == 1:
        press_key()
        time.sleep(frame_time)
        
        release_key()
    time.sleep(0.01)
import time
import win32api
import win32con

# FPS 설정
frame_time = 0.1

# 'gaming' 상태 (0: 대기, 1: 기록 중)
gaming = 0  

# Enter 키 입력 시 gaming 값 토글
import keyboard
def toggle_gaming():
    global gaming
    gaming = 1 - gaming
    if gaming == 1:
        print("keyDown started!")
    else:
        print("keyDown stopped!")

keyboard.add_hotkey("enter", toggle_gaming)

print("Press 'Enter' to start/stop recording...")

while True:
    if gaming == 1:
        win32api.keybd_event(0x57, 0, 0, 0)  # 'W' 키 눌림
        time.sleep(frame_time)
        win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)  # 'W' 키 뗌
    time.sleep(0.01)

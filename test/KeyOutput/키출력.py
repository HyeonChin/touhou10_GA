import time
import keyboard
import pyautogui
        
def press_key(key, frame_time):
    pyautogui.keyDown(key)
    time.sleep(frame_time)
    pyautogui.keyUp(key)

# FPS 설정
fps = 60  
frame_time = 1 / fps
frame_time = 0.1

# 'gaming' 상태 (0: 대기, 1: 기록 중)
gaming = 0  

start_time = None  # 기록 시작 시간

# Enter 키 입력 시 gaming 값 토글
def toggle_gaming():
    global gaming, start_time, z_key_frames
    gaming = 1 - gaming  # 0 ↔ 1 전환
    if gaming == 1:
        print("keyDown started!")
        start_time = time.time()  # 시작 시간 초기화
    else:
        print("keyDown stopped!")

# Enter 키 이벤트 리스너 등록
keyboard.add_hotkey("enter", toggle_gaming)

print("Press 'Enter' to start/stop recording...")

# 메인 루프

while True:
    if gaming == 1:
        press_key('w', frame_time)
    elif gaming == 0 and start_time is not None:
        start_time = None  # 출력 종료 후 초기화
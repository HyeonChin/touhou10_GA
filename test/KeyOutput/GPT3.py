import time
import ctypes
from ctypes import wintypes
import keyboard

# 필요한 Windows API 설정
SendInput = ctypes.windll.user32.SendInput

# 키보드 이벤트 구조체 설정
PUL = ctypes.POINTER(ctypes.c_ulong)

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", wintypes.WORD),
                ("wScan", wintypes.WORD),
                ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD),
                ("dwExtraInfo", PUL)]

class INPUT_I(ctypes.Union):
    _fields_ = [("ki", KEYBDINPUT)]

class INPUT(ctypes.Structure):
    _fields_ = [("type", wintypes.DWORD),
                ("ii", INPUT_I)]

# 가상 키 코드
VK_W = 0x57

# KEYEVENTF 상수
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

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
def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = INPUT_I()
    ii_.ki = KEYBDINPUT(hexKeyCode, 0, KEYEVENTF_KEYDOWN, 0, ctypes.pointer(extra))
    x = INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = INPUT_I()
    ii_.ki = KEYBDINPUT(hexKeyCode, 0, KEYEVENTF_KEYUP, 0, ctypes.pointer(extra))
    x = INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# 메인 루프
while True:
    if gaming == 1:
        press_key(VK_W)
        time.sleep(frame_time)
        release_key(VK_W)
    time.sleep(0.01)
import pyautogui

def activate_window(title):
    windows = pyautogui.getWindowsWithTitle(title)
    if windows:
        windows[0].activate()
        print(f"'{title}' 창 있음")
    else:
        print(f"'{title}' 창 없음")

def get_all_window_names():
    for window in pyautogui.getAllWindows():
        print(window.title)
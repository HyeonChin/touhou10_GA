import pyautogui

def activate_window(title):
    windows = pyautogui.getWindowsWithTitle(title)
    if windows:
        windows[0].activate()
        return windows[0].box
    return False

def get_all_window_names():
    for window in pyautogui.getAllWindows():
        print(window.title)
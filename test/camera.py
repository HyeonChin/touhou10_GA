import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab


rel_x1, rel_y1, rel_x2, rel_y2 = 170, 240, 270, 300

width = rel_x2 - rel_x1
height = rel_y2 - rel_y1

def activate_window(title):
    windows = pyautogui.getWindowsWithTitle(title)
    if windows:
        windows[0].activate()
        return windows[0].box
    return False

def capture_area_around_cursor(window_box):
    left, top, width, height = window_box
    
    x1, y1 = left+rel_x1, top+rel_y1
    x2, y2 = left+rel_x2, top+rel_y2
    
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    
    return np.array(screen)

def show_live_capture(window_box):
    cv2.namedWindow("Live Capture")
    while True:
        global width
        global height

        cap_img = capture_area_around_cursor(window_box)
        cv2.imshow("Live Capture", cv2.cvtColor(cap_img, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(1) == ord('q'):  # 'q' 키를 누르면 종료
            break
    cv2.destroyAllWindows()

window_box = activate_window('동방')
if window_box:
    show_live_capture(window_box)
else:
    print("동방")
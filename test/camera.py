import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab

import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

rel_x1, rel_y1, rel_x2, rel_y2 = 170, 240, 270, 300

width = rel_x2 - rel_x1
height = rel_y2 - rel_y1

def activate_window(title):
    windows = pyautogui.getWindowsWithTitle(title)
    if windows:
        windows[0].activate()
        return windows[0].box
    return False

def capture_area(window_box):
    left, top, width, height = window_box
    
    x1, y1 = left+rel_x1, top+rel_y1
    x2, y2 = left+rel_x2, top+rel_y2
    
    screen = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    
    return np.array(screen)

def show_live_capture(window_box, isShow):
    cv2.namedWindow("Live Capture")
    while True:
        global width
        global height

        cap_img = capture_area(window_box)
        if isShow:
            cv2.imshow("Live Capture", cv2.cvtColor(cap_img, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(1) == ord('q'):  # 'q' 키를 누르면 종료
            cv2.destroyAllWindows()
            return cap_img


def convert_img_to_text(cap_img):
    image = cv2.resize(cap_img, dsize=(width*3,height*3))
            
    # PIL Image 객체를 NumPy 배열로 변환합니다.
    image_np = np.array(image)

    # NumPy 배열을 OpenCV 이미지(BGR)로 변환합니다.
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # OpenCV 이미지를 그레이스케일로 변환합니다.
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Tesseract OCR 설정
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray_image, config=custom_config, lang="kor")
    return text

window_box = activate_window('동방')
if window_box:
    cap_img = show_live_capture(window_box, isShow=True)
    text = convert_img_to_text(cap_img)

    if text:
        #텍스트 전체 인식
        text = text.replace(" ", "")
        print("인식된 텍스트:", text)

        # 숫자 인식 후 변수에 저장 및 출력
        numbers = re.findall(r'\d+', text)
        if numbers:
            print("인식된 숫자:", numbers)
        else:
            print("숫자 인식 불가")
    else:
        print("텍스트 인식 불가")
else:
    print("동방")
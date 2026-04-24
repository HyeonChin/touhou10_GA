import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time
import random
import pytesseract
import re

import sys


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

window_box = 0
def activate_window(title):
    global window_box

    windows = pyautogui.getWindowsWithTitle(title)
    if windows:
        windows[0].activate()
        window_box = windows[0].left, windows[0].top, windows[0].width, windows[0].height
        print(f"'{title}' 창 있음")
    else:
        print(f"'{title}' 창 없음")
    
def recognized_data(rel_x1, rel_y1, rel_x2, rel_y2, type, custom_config=r'--oem 3 --psm 6', costom_lang="kor"):
    global window_box
    left, top, width, height = window_box
    
    x1, y1 = left+rel_x1, top+rel_y1
    x2, y2 = left+rel_x2, top+rel_y2
    
    # bbox 인자를 사용하여 화면의 특정 부분을 캡처합니다.
    cap_img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    cap_img_np = np.array(cap_img)
    
    # 이미지 크기 조정
    image = cv2.resize(cap_img_np, dsize=((x2-x1)*3,(y2-y1)*3))
    image_np = np.array(image)

    # NumPy 배열을 OpenCV 이미지(BGR)로 변환합니다.
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    # OpenCV 이미지를 그레이스케일로 변환합니다.
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    
    # Tesseract OCR 설정
    text = pytesseract.image_to_string(gray_image, config=custom_config, lang=costom_lang)

    # 텍스트 전체 인식
    print("인식된 텍스트:", text)
    text = text.strip()

    if type == "number":
        # 숫자 인식 후 변수에 저장 및 출력
        numbers = re.findall(r'\d+', text)
        
        try:
            number = numbers[0]
            return int(number)
        except:
            return "error"
    elif type == "text":
        return text
    
def repeat_recognize(start_time, end_time, unit_time, break_condition, recognized_func, *func_args):
    time.sleep(start_time / 1000)

    t = start_time
    while True:
        # recognized_func에 전달된 함수를 호출하여 텍스트를 동적으로 인식
        text = recognized_func(*func_args)
        
        if break_condition(text):
            print(f"인식 완료: {text}")
            break
        elif t >= end_time:
            break
        else:
            time.sleep(unit_time / 1000)
            t += unit_time
            print(f"소요 시간: {t}")

    return text
            
def decide_ticket_purchase():
    global pre_tickets_number

    start_time, end_time, unit_time = 0, 5000, 500
    
    number = repeat_recognize(
        start_time, end_time, unit_time,
        lambda text: text != "error",
        recognized_data,
        330, 968, 400, 988, "number"
    )

    if number == "error":
        tickets_number = pre_tickets_number - 1
        
        log_data = "tickets_number_error: " + current_time() + "\n"
        record_log("tickets_number_error_report.txt", log_data)
    else:
        tickets_number = number
        
    print("남은 도전권 수:", tickets_number)
    #record_log()

    if tickets_number == 1:
        # 로그 기록
        time.sleep(20)

        matches_number = recognized_data(80, 100, 200, 120, "number")
        log_time = current_time()

        log_data = f"{matches_number}, {log_time}\n"
        record_log("log.txt", log_data)

        #종료
        sys.exit()

        keys = [('d', random.uniform(1.0, 1.2)), ('s', random.uniform(1.0, 1.6)), ('a', random.uniform(1.0, 1.6)), ('s', random.uniform(1.0, 1.2)), ('a', random.uniform(0.5, 0.9))]
        press_key(keys)
        
    pre_tickets_number = tickets_number

def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def record_log(file_name, log_data):
    f = open(file_name, 'a')
    print(log_data)
    f.write(log_data)
    f.close

def run_game():
    # 바로 포기
    '''
    keys = [('s', 3.8), ('a', 2.5)]
    press_key(keys)
    '''

    
    # 바로 포기 - 동적 시간지연
    keys = [('s', 0)]
    press_key(keys)

    start_time, end_time, unit_time = 3000, 30000, 500

    repeat_recognize(
        start_time, end_time, unit_time,
        lambda text: text == "ROUND",
        recognized_data, 
        230, 165, 330, 190, "text", r'--oem 3 --psm 6 -c tessedit_char_whitelist=ROUND', "eng"
    )

    keys = [('a', 2.5)]
    press_key(keys)

    multiple = recognized_data(350, 998, 360, 1020, "number")
    record_log("multiple_log.txt", str(multiple) + "\n")
    
    match_obtained = recognized_data(301, 820, 328, 845, "number")
    record_log("match_obtained_log.txt", str(match_obtained) + "\n")

    keys = [('b', 0.2), ('a', 0.7)]
    press_key(keys)

    '''
    # 다음 라운드 무한 도전
    keys = [('s', 3.2), ('a', 2.4)]
    press_key(keys)
    run_game_random(1)
    '''
    run_game()

def run_game_random(round, pre_multiple=0):
    multiple = recognized_data(350, 998, 360, 1020, "number")

    # 최초 도전이 아니라면
    if(round != 1):
        log_data = str(pre_multiple)

        # 실패 시
        if(multiple == "error"):
            log_data += "/failure\n"
            record_log("randomLog.txt", log_data)

            keys = [("s", 0.5)]
            press_key(keys)
            return 0
        else:
            log_data += "/success\n"
            record_log("randomLog.txt", log_data)

    if multiple == 2:
        keys = [('s', 0.1), ('a', 3.2), ('a', 2.4)]
        press_key(keys)
        run_game_random(round+1, pre_multiple=multiple)
    else:
        keys = [('b', 0.1), ('a', random.uniform(0.0, 0.2))]
        press_key(keys)
        
def press_key(keys):
    if len(keys) == 1:
        key, delay = keys[0]
        print(key, delay)
        pyautogui.press(key)
        time.sleep(delay)
    else:
        for key, delay in keys:
            print(key, delay)
            pyautogui.press(key)
            time.sleep(delay)
    return 0

def escape_shop():
    global shop_error_stack
    text = recognized_data(260, 70, 340, 100, "text")

    if text == "불 꽃 상 점":
        shop_error_stack+=1
        log_data = f"shop_error({shop_error_stack}): {current_time()}\n"
        record_log("shop_error_report.txt", log_data)

        keys = [("e", 1.0)]
        press_key(keys)
    return 0

pyautogui.FAILSAFE = False

# 오류 검출용
pre_tickets_number = 100
shop_error_stack = 0

#record_log("log.txt", "start\n")

activate_window('LDPlayer')

# 이 함수에 반복을 설정할 수 있음
run_game()

# 티켓 다 돌리고 종료되도록 설정함
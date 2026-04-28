import camera
import cv2
import numpy as np

# 게임오버 화면 템플릿 이미지를 미리 캡처해서 저장
template = cv2.imread('./assets/gameover_template.png', cv2.IMREAD_GRAYSCALE)

def isGameOver(window_box):
    gameover_msg_coordinate = [170, 240, 270, 300]
    image_np = camera.capture_area(window_box, gameover_msg_coordinate)
    
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    if max_val > 0.5: # 유사도 50% 이상이면 게임오버
        return
    
import numpy as np
from PIL import ImageGrab


def capture_area(window_box, area_coordinate):
    left, top = window_box[:2]
    rel_x1, rel_y1, rel_x2, rel_y2 = area_coordinate
    
    x1, y1 = left+rel_x1, top+rel_y1
    x2, y2 = left+rel_x2, top+rel_y2
    
    cap_img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # PIL Image 객체를 NumPy 배열로 변환
    image_np = np.array(cap_img)
    
    return image_np
import camera
import converter

def isGameOver(window_box):
    gameover_msg_coordinate = [170, 240, 270, 300]
    image_np = camera.capture_area(window_box, gameover_msg_coordinate)

    text = converter.convert_img_to_text(image_np)
    if text == "게임오버!":
        return True
    else:
        return False
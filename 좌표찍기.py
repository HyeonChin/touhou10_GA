import window
import camera
import converter

gameover_msg_coordinate = [170, 240, 270, 300]

window_box = window.activate_window("동방")
if window_box:
    cap_img = camera.capture_live_area(window_box, area_coordinate=gameover_msg_coordinate, isShow=True)
    text = converter.convert_img_to_text(cap_img)
    if text:
        print(f"인식된 텍스트: {text}")

    number = converter.convert_text_to_number(text)
    if number:
        print(f"인식된 숫자: {number}")
else:
    print("동방")
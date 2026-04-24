import window
import camera
import converter
import cv2

gameover_msg_coordinate = [170, 240, 270, 300]

window_box = window.activate_window("동방")
if window_box:
    cv2.namedWindow("Live Capture")
    while True:
        image_np = camera.capture_area(window_box, gameover_msg_coordinate)
        cv2.imshow("Live Capture", cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))

        text = converter.convert_img_to_text(image_np)
        if text:
            print(f"인식된 텍스트: {text}")
            if text == "게임오버!":
                print("!")
            else:
                print(f"게임오버! != {repr(text)}")

        number = converter.convert_text_to_number(text)
        if number:
            print(f"인식된 숫자: {number}")

        if cv2.waitKey(1) == ord('q'):  # 'q' 키를 누르면 종료
            cv2.destroyAllWindows()
            break
else:
    print("동방")
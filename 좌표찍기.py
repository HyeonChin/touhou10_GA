import window
import camera
import converter
import cv2

gameover_msg_coordinate = [170, 240, 270, 300]

window_box = window.activate_window("동방")
if window_box:
    cv2.namedWindow("Live Capture")
    print("게임오버 화면에서 's' 키를 눌러 템플릿 저장")
    while True:
        image_np = camera.capture_area(window_box, gameover_msg_coordinate)
        cv2.imshow("Live Capture", cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))

        text = converter.convert_img_to_text(image_np)
        if text:
            print(f"인식된 텍스트: {text}")

        key = cv2.waitKey(1)

        if key == ord('s'):  # 's' 키로 템플릿 저장
            gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
            cv2.imwrite('./assets/gameover_template.png', gray)
            print("템플릿 저장 완료: ./assets/gameover_template.png")
        elif key == ord('q'):  # 'q' 키를 누르면 종료
            cv2.destroyAllWindows()
            break
else:
    print("동방 창을 찾을 수 없습니다.")
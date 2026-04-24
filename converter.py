import cv2
import pytesseract
import re

def convert_img_to_text(image_np):
    # NumPy 배열의 이미지 크기를 늘림
    mag = 3     # magnification
    image_np = cv2.resize(image_np, dsize=(image_np.shape[1]*mag, image_np.shape[0]*mag))

    # NumPy 배열을 OpenCV 이미지(BGR)로 변환
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # OpenCV 이미지를 그레이스케일로 변환
    gray_image = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Tesseract OCR 설정
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray_image, config=custom_config, lang="kor")

    if text:
        # 텍스트 전체 인식
        text = text.strip().replace(" ", "")
        return text
    else:
        # 텍스트 인식 불가
        return None

def convert_text_to_number(text):
    if text is None:
        return None

    numbers = re.findall(r'\d+', text)

    if numbers:
        return numbers
    else:
        return None

    
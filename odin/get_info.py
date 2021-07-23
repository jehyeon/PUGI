from PIL import Image
import pytesseract
import cv2
import pyautogui

# QHD, 1/4 좌상단 기준 (temporary)
# 체력과 포션의 경우 단위가 달라질 수가 있음을 고려해야 함
HP_REGION = (72, 42, 80, 15)
LEVEL_REGION = (9, 655, 49, 37)
EXP_REGION = (83, 673, 57, 15)
# BUFF_REGION = [
#     (499, 655, 27, 18),
#     (559, 657, 25, 16),
#     (629, 657, 25, 16),
#     (691, 657, 25, 16),
#     (753, 657, 25, 16)
# ]
# PORTION_REGION = (1145, 510, 30, 17)

def capture():
    # temp
    pyautogui.screenshot('logs/hp.png', region=HP_REGION)
    pyautogui.screenshot('logs/level.png', region=LEVEL_REGION)
    pyautogui.screenshot('logs/exp.png', region=EXP_REGION)
    # pyautogui.screenshot('logs/buff1.png', region=BUFF_REGION[0])
    # pyautogui.screenshot('logs/buff2.png', region=BUFF_REGION[1])
    # pyautogui.screenshot('logs/buff3.png', region=BUFF_REGION[2])
    # pyautogui.screenshot('logs/buff4.png', region=BUFF_REGION[3])
    # pyautogui.screenshot('logs/portion.png', region=PORTION_REGION)
    
def imageToText(fileName):
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
    
    img = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
    # img = convertGrayScale(img)
    h, w = img.shape
    img = cv2.resize(img, (w * 2, h * 2))
    retval2, th = cv2.threshold(img, 5, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return pytesseract.image_to_string(th, lang='eng')
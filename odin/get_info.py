from PIL import Image
import pytesseract
import cv2
import pyautogui
import numpy as np

# QHD, 1/4 좌상단 기준 (temporary)
# 체력과 포션의 경우 단위가 달라질 수가 있음을 고려해야 함
HP_REGION = (72, 42, 80, 15)

# LEVEL_REGION = (9, 655, 49, 37)
# EXP_REGION = (83, 673, 57, 15)

QUEST_REGION = (1064, 110, 45, 23)
QUEST_CLEAR_REGION = (267, 137, 42, 50)
QUEST_CLEAR_TEXT = ['2z']

REMAIN_POTION_REGION = (608, 308, 65, 35)

# BUFF_REGION = [
#     (499, 655, 27, 18),
#     (559, 657, 25, 16),
#     (629, 657, 25, 16),
#     (691, 657, 25, 16),
#     (753, 657, 25, 16)
# ]
# PORTION_REGION = (1145, 510, 30, 17)

QUESRT_CLEAR_TEMP = (1024, 130, 124, 23)

def captureT(region):
    print('?')
    _region = (region[0], region[1], region[2] - region[0], region[3] - region[1])
    pyautogui.screenshot('logs/temp.png', region=_region)

def compareImage(fileName, region, comparingImage):
    _region = (region[0], region[1], region[2] - region[0], region[3] - region[1])
    pyautogui.screenshot(fileName, region=_region)

    img1 = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(comparingImage, cv2.IMREAD_GRAYSCALE)

    # 이미지 이진화
    retval2, th1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
    retval2, th2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)

    # diff1 = cv2.subtract(th1 + th2, th2)
    # diff2 = cv2.subtract(th2, th1 + th2)
    # blur = cv2.blur(diff, (5,5))

    # cv2.imshow('temp2', th2)
    cv2.imshow('temp1', th1)
    cv2.imshow('temp2', th2)
    temp = th1 == th2
    result = np.where(temp == True, 255, 0)
    cv2.imwrite(fileName, result)
    # cv2.imshow('temp', result)
    cv2.waitKey(0)

    # th1 - th2
    # cv2.waitKey(0)

    # 이미지 비교 후 블러 처리한 array의 최대 값이 20 이하면 같은 이미지로 판별
    # if np.max(diff) < 20:
    #     print('True')
    #     return True

    # print('False')
    # return False

def getImageToText(fileName, region):
    _region = (region[0], region[1], region[2] - region[0], region[3] - region[1])
    pyautogui.screenshot(fileName, region=_region)

    return imageToText(fileName)

def capture():
    # temp
    pyautogui.screenshot('logs/temp.png', region=QUESRT_CLEAR_TEMP)
    # pyautogui.screenshot('logs/hp.png', region=HP_REGION)
    # pyautogui.screenshot('logs/remain_potion.png', region=REMAIN_POTION_REGION)
    # pyautogui.screenshot('logs/quest_clear.png', region=QUEST_CLEAR_REGION)
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
    img = cv2.resize(img, (w * 3, h * 3))
    retval2, th = cv2.threshold(img, 5, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # cv2.imshow('temp', th)
    # cv2.waitKey(0)

    return pytesseract.image_to_string(th, lang='kor').strip().replace(' ', '')

# Status 가져오기
def getStatus():
    # temp
    capture()

    level = imageToText('logs/level.png')
    exp = imageToText('logs/exp.png')
    hp = imageToText('logs/hp.png')

    return level, exp, hp

def checkQuestClear():
    # 퀘스트 완료 여부
    count = 0
    clear = False
    while count < 3 and not clear:
        pyautogui.screenshot('logs/quest_clear.png', region=QUEST_CLEAR_REGION)
        print('{0}차 확인: {1}'.format(count + 1, imageToText('logs/quest_clear.png')))
        if imageToText('logs/quest_clear.png') in QUEST_CLEAR_TEXT:
            clear = True
        count += 1

    return clear



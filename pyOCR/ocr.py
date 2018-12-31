from PIL import Image
from pytesseract import *
import cv2

def OCR(_image, lang='eng'):
    image = Image.open(_image)
    text = image_to_string(image, lang=lang)

    return text

# print(OCR('text_image.png'))
# print(OCR('text_image_kr.png', 'kor'))

# print(OCR('test.jpg'))

def thresholding(_image):
    gray = cv2.imread(_image, cv2.IMREAD_GRAYSCALE)
    
    # Enlarge 2x
    height, width = gray.shape
    gray_enlarge = cv2.resize(gray, (width*2, height*2), interpolation=cv2.INTER_LINEAR)

    # Denoising
    denoised = cv2.fastNlMeansDenoising(gray, h=10, searchWindowSize=21, templateWindowSize=7)

    # blur = cv2.GaussianBlur(gray, (3,3), 0)
    ret, thr = cv2.threshold(denoised, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    print(image_to_string(thr, lang='eng'))

    cv2.imshow("thr", thr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


thresholding('test1.jpg')
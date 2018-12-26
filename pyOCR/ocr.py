from PIL import Image
from pytesseract import *

def OCR(_image, lang='eng'):
    image = Image.open(_image)
    text = image_to_string(image, lang=lang)

    return text

# print(OCR('text_image.png'))
# print(OCR('text_image_kr.png', 'kor'))

print(OCR('test.jpg'))
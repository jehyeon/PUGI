# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


from PIL import Image, ImageFilter
from pytesseract import image_to_string

def OCR(imgfile, language):
    text = image_to_string(image, lang=language)
    print(text)

def main():
    image = Image.open('../data/PUBG_screenshot.png')

    img = cv2.imread('../data/PUBG_screenshot.png')

    equipPos_x = int(img.shape[1] * 2 / 3)

    temp = image.crop((equipPos_x, 0, equipPos_x / 2 + 100, img.shape[0] + 100))
    # print(type(img.shape))
    temp.save('./a.png')

    # img = cv2.imread('../data/PUBG_screenshot.png', cv2.IMREAD_GRAYSCALE)
    #
    # eg1 = cv2.Canny(img, 50, 200)
    # eg2 = cv2.Canny(img, 100, 200)
    # eg3 = cv2.Canny(img, 170, 200)
    #
    # cv2.imshow('origin', img)
    # cv2.imshow('Canny Edge1', eg1)
    # cv2.imshow('Canny Edge2', eg2)
    # cv2.imshow('Canny Edge3', eg3)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Set Blur Image
    # blur = image.filter(ImageFilter.GaussianBlur)
    # blur.save('../data/blur.png')
    # blur.show()


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
import ESwh as es

from PIL import Image, ImageFilter
from pytesseract import image_to_string

def OCR(imgfile, language):
    text = image_to_string(imgfile, lang=language)
    print(text)

# img, xy : start pos, wh : width x height
# def im_trim (img, xy, wh):
#     img_trim = img[]
def main():
    src = '../data/PUBG_screenshot.png'
    image = es.ESwh(src)

    image.save_all('./')

def main2():
    src  = '../data/PUBG_screenshot.png'
    # image = IPos(src)
    image = Image.open(src)

    width, height = image.size
    print(width, height)
    # size = image.getSize()
    # print("Origin size: " + str(size))
    # print("area = {0}, {1}, {2}, {3}".format(int(width/3 * 2), 0, width, height))
    area = (int(width/3 * 2), 0, width, height)
    cropped = image.crop(area)
    # cropped.show()

    # Read image and covert COLOR_GRAY
    img = cv2.imread(src, cv2.IMREAD_COLOR)
    height, width, _ = img.shape
    print(width, height)
    # cv2.imwrite('tempo.jpg',img[0:height,int(width/3*2):width])
    cropped = img[0:height,int(width/3*2):width].copy()
    img_gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

    # Blur image and save
    blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    cv2.imwrite('blur.jpg', blur)

    # Edge detection
    canny = cv2.Canny(blur, 200, 300)
    cv2.imwrite('canny.jpg', canny)

    box1 = []

    # Contours
    cnts, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        rect_area = w*h             # area size
        aspect_ratio = float(w)/h   # ratio = width/height

        if (aspect_ratio >= 0.5) and (aspect_ratio <= 2.0) and (rect_area >= 15) and (rect_area <= 100):
            cv2.rectangle(cropped, (x,y), (x+w,y+h),(0,255,0),1)
            box1.append(cv2.boundingRect(cnt))

    cv2.imwrite('temp.jpg', cropped)
    print(box1)
    # size_x = size[1]/3 - size[1]/3 * 2
    # width = int(size[1] - size_x)

    # image.trim((int(size[0]/3 * 2), size[1]), (width, size[1]))

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
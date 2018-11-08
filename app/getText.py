# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt


from PIL import Image, ImageFilter
from pytesseract import image_to_string

# Class for coordinate calculation
class XY:
    def __init__(self, x, y):
        self.pos = (x, y)

# ImagePos needs cv2
class IPos:
    def __init__(self, src):
        self._image = cv2.imread(src)
        self._h, self._w, _ = self._image.shape

    # return width, height
    def getSize(self):
        self._wh = XY(self._w, self._h)
        return self._w, self._h

    # pos, wh is tuple (x, y)
    def trim(self, pos, wh):
        image_trim = self._image[int(pos[1]):int(wh[1]), int(pos[0]):int(wh[0])]
        # temp
        print('pos : ' + str(int(pos[1])) + ' ' + str(int(pos[0])))
        print('width x height : '+ str(int(wh[1])) + ' ' + str(int(wh[0])))
        ###
        cv2.imwrite('image_trim.jpg', image_trim)
        return image_trim


def OCR(imgfile, language):
    text = image_to_string(imgfile, lang=language)
    print(text)

# img, xy : start pos, wh : width x height
# def im_trim (img, xy, wh):
#     img_trim = img[]

def main():
    src  = '../data/PUBG_screenshot.png'
    image = IPos(src)

    size = image.getSize()
    size_x = size[1]/3 - size[1]/3 * 2
    width = int(size[1] - size_x)

    image.trim((int(size[0]/3 * 2), size[1]), (width, size[1]))

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
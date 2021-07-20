import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui

# 651 807
# diff 400 20

while (True):
    pic = pyautogui.screenshot(region=(651, 807, 400, 20))
    frame = np.array(pic)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    cv2.imshow('result', frame)
# screen = ImageGrab.grab()
# screen = np.array(screen)
# cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
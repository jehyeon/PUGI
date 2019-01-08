import numpy as np
from PIL import ImageGrab
import cv2

count = 0
while (True):
    screen = ImageGrab.grab()
    screen = np.array(screen)
    print(count)
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    count += 1
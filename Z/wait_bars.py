import cv2 as cv
import numpy as np
import time
from PIL import ImageGrab

def wait_bars(temp):
    temp = f'{temp}.bmp'
    while True:
        time.sleep(1)
        img_rgb = ImageGrab.grab()
        img_rgb = np.array(img_rgb)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

        template = cv.imread(temp, cv.IMREAD_GRAYSCALE)
        w,h = template.shape[::-1]
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.8

        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            time.sleep(1)
            break

        else: break
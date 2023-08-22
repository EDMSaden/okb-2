import cv2 as cv
import numpy as np
from PIL import ImageGrab
#Для проверки шаблона внесите в аргумент test искомый шаблон и запустите данный файл
#Все шаблоны должны быть в формате .bmp
test = r'test'

def lf_template(temp):
    temp = f'{temp}.bmp'
    img_rgb = ImageGrab.grab()
    img_rgb = np.array(img_rgb)
    img_rgb = cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    template = cv.imread(temp, cv.IMREAD_GRAYSCALE)
    w,h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):          
        if __name__ == '__main__':
            cv.rectangle(img_rgb,pt,(pt[0] + w, pt[1] + h), (0,0,255), 2)
            print(pt[0] + int(w/2), pt[1] + int(h/2))
            break
        else:
            return pt[0] + int(w/2), pt[1] + int(h/2)
        
    if __name__ == '__main__':
        img_rgb = cv.resize(img_rgb, (1024, 768))
        cv.imshow('result', img_rgb)
        cv.waitKey(0)


    
if __name__ == '__main__':
    while True:
        lf_template(test)
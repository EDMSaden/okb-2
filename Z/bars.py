import cv2 as cv
import numpy as np
import time
from PIL import ImageGrab
import win32api, win32con
import pyperclip

def leftClick(*cord):
    if len(cord) == 1:
        cord = cord[0] 
    x,y = cord 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.003)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def rightClick(*cord):
    if len(cord) == 1:
        cord = cord[0] 
    x,y = cord 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
    time.sleep(0.003)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)


def doubleClick(*cord):
    if len(cord) == 1:
        cord = cord[0] 
    x,y = cord
    for i in range(2):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(0.003)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


keys = {'CTRL':0x11, 'ENTER':0x0D, 'PAGEUP':0x21,
        'PAGEDOWN':0x22, 'ESC':0x1B , 'BACKSPACE':0x08, 'SPACE':0x20, 'SHIFT':0x10}

def find_key(key : str):
    key = key.upper()
    if key in keys:
        key = keys.get(key)
    else: key = ord(key)
    return key

def press_key(key : str):

    key = find_key(key)
    win32api.keybd_event(key, 0,0,0)
    time.sleep(.05)   
    win32api.keybd_event(key,0 ,win32con.KEYEVENTF_KEYUP ,0)

def hot_key(key_1 : str, key_2 : str):
    key_1 = find_key(key_1)
    key_2 = find_key(key_2)
    win32api.keybd_event(key_1, 0,0,0)
    time.sleep(.05)
    win32api.keybd_event(key_2, 0,0,0)
    time.sleep(.05)

    win32api.keybd_event(key_1,0 ,win32con.KEYEVENTF_KEYUP ,0)
    win32api.keybd_event(key_2,0 ,win32con.KEYEVENTF_KEYUP ,0)


def write_text(text : str):
    pyperclip.copy(text)
    hot_key('ctrl', 'v')

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

def change_row(cord,text):
    leftClick(cord)
    hot_key('ctrl','a')
    write_text(f'{text}')
    time.sleep(1)
    wait_bars('wait_1')
    press_key('enter')
    wait_bars('wait_1')

    
if __name__ == '__main__':
    while True:
        lf_template(test)
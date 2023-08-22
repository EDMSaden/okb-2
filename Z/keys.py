import win32api, win32con
import time
# https://learn.microsoft.com/ru-ru/windows/win32/inputdev/virtual-key-codes

keys = {'CTRL':0x11, 'ENTER':0x0D, 'PAGE_UP':0x21,
        'PAGE_DOWN':0x22, 'ESC':0x1B , 'BACKSPACE':0x08, 'SPACE':0x20, 'SHIFT':0x10}

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

hot_key('a', 'ы')# for i in 'Привет':# for i in 'Привет':asфыфыфыasфыф

# for i in 'Привет':
#     print(ord(i))

# [print(ord(i)) for i in 'Привет']
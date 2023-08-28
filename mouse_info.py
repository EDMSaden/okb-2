import win32api
import time
import pyperclip

#Нажмите F2 получите координаты

if __name__ == '__main__':
    while True:
        if win32api.GetKeyState(0x71) < 0:
            print(f'{win32api.GetCursorPos()[0]}, {win32api.GetCursorPos()[1]}')
            pyperclip.copy(f'{win32api.GetCursorPos()[0]}, {win32api.GetCursorPos()[1]}')
            time.sleep(.5)
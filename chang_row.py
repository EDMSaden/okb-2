import time
import pyautogui
from wait_bars import wait_bars
def change_row(cord,write_text):
    pyautogui.moveTo(cord)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrlleft','a')
    pyautogui.write(f'{write_text}')
    time.sleep(1)
    wait_bars('wait_1.bmp')
    pyautogui.press('enter')
    wait_bars('wait_1.bmp')

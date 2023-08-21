import pyautogui
import time
from wait_bars import wait_bars
from lf_template import lf_template
from chang_row import change_row

distance = 0

for i in range(5):

    if lf_template(r'start.bmp'):
        pyautogui.moveTo(70,450 + distance)
        distance += 34
        pyautogui.leftClick()
        wait_bars(r'wait_1.bmp')

        pyautogui.moveTo(1056,219)
        pyautogui.leftClick()
        wait_bars(r'wait_1.bmp')

        if lf_template(r'filter.bmp'):
            pyautogui.moveTo(lf_template(r'filter.bmp', coordinates=True))
            pyautogui.leftClick()
            wait_bars(r'wait_1.bmp')
            pyautogui.moveTo(440,241)
            pyautogui.leftClick()
            wait_bars(r'wait_1.bmp')
            pyautogui.hotkey('ctrl', 'v')
            
            pyautogui.moveTo(68,218)
            pyautogui.doubleClick()
            wait_bars(r'wait_1.bmp')
            pyautogui.rightClick()
            wait_bars(r'wait_1.bmp')
            if lf_template(r'list.bmp'):
                pyautogui.moveTo(lf_template(r'list.bmp', coordinates=True))
                pyautogui.leftClick()
                wait_bars(r'wait_1.bmp')
                if lf_template(r'neot.bmp'):
                    pyautogui.moveTo(lf_template(r'neot.bmp', coordinates=True))
                    pyautogui.doubleClick()
                    wait_bars(r'wait_1.bmp')
                    if lf_template(r'yellow.bmp'):
                        change_row(lf_template(r'yellow.bmp', coordinates=True), 1)
                        wait_bars(r'wait_1.bmp')
                        pyautogui.press('pagedown')
                        wait_bars(r'wait_1.bmp')
                        pyautogui.moveTo(lf_template(r'save.bmp', coordinates=True))
                        pyautogui.leftClick()
                        wait_bars(r'wait_1.bmp')
                        pyautogui.leftClick()
                        wait_bars(r'wait_1.bmp')

    pyautogui.press('esc')
    wait_bars(r'wait_1.bmp')               







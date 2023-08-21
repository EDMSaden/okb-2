import pyautogui
from wait_bars import wait_bars
from lf_template import lf_template
from chang_row import change_row
from time import sleep

sleep(3)
distance = 0
while True:
    for i in range(12):
        if lf_template(r'start_1.bmp') and lf_template(r'start_2.bmp'):
            pyautogui.moveTo(55,446 + distance)
            distance += 30
            pyautogui.leftClick()
            wait_bars(r'wait_1.bmp')

            if lf_template(r'pos.bmp'):
                change_row((986,245),2)
                wait_bars(r'wait_1.bmp')
                change_row((974,270),2)
                wait_bars(r'wait_1.bmp')
                change_row((702,470),6)
                wait_bars(r'wait_1.bmp')
                change_row((692,494),1)
                wait_bars(r'wait_1.bmp')
                if lf_template(r'result_1.bmp') and lf_template(r'result_2.bmp'):
                    pyautogui.press('pagedown')
                    wait_bars(r'wait_1.bmp')
                    pyautogui.moveTo(lf_template(r'save.bmp',coordinates=True))
                    pyautogui.leftClick()
                    wait_bars(r'wait_1.bmp')
                    pyautogui.leftClick()
                    wait_bars(r'wait_1.bmp')

        pyautogui.press('esc')
        wait_bars(r'wait_1.bmp')               
    
    if lf_template(r'ok.bmp'):
        pyautogui.moveTo(lf_template(r'ok.bmp',coordinates=True))
        pyautogui.leftClick()
        distance = 0
        wait_bars(r'wait_1.bmp')  
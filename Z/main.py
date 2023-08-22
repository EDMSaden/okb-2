from pyautogui import moveTo, leftClick, rightClick, doubleClick, press, hotkey
from wait_bars import wait_bars
from lf_template import lf_template
from chang_row import change_row
from time import sleep

sleep(3)
distance = 0
while True:
    for i in range(12):
        if lf_template('start_1') and lf_template('start_2'):
            moveTo(55,446 + distance)
            distance += 30
            leftClick()
            wait_bars('wait_1')

            if lf_template('pos'):
                change_row((986,245),2)
                wait_bars('wait_1')
                change_row((974,270),2)
                wait_bars('wait_1')
                change_row((702,470),6)
                wait_bars('wait_1')
                change_row((692,494),1)
                wait_bars('wait_1')
                if lf_template('result_1') and lf_template('result_2'):
                    press('pagedown')
                    wait_bars('wait_1')
                    moveTo(lf_template('save'))
                    leftClick()
                    wait_bars('wait_1')
                    leftClick()
                    wait_bars('wait_1')

        press('esc')
        wait_bars('wait_1')               
    
    if lf_template('ok'):
        moveTo(lf_template('ok'))
        leftClick()
        distance = 0
        wait_bars('wait_1')  
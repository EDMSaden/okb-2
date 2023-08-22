from pyautogui import moveTo, leftClick, rightClick, doubleClick, press, hotkey
from time import sleep
from wait_bars import wait_bars
from lf_template import lf_template
from chang_row import change_row

distance = 0

for i in range(5):

    if lf_template('start'):
        moveTo(70,450 + distance)
        distance += 34
        leftClick()
        wait_bars('wait_1')

        moveTo(1056,219)
        leftClick()
        wait_bars('wait_1')

        if lf_template('filte'):
            moveTo(lf_template('filte'))
            leftClick()
            wait_bars('wait_1')
            moveTo(440,241)
            leftClick()
            wait_bars('wait_1')
            hotkey('ctrl', 'v')
            
            moveTo(68,218)
            doubleClick()
            wait_bars('wait_1')
            rightClick()
            wait_bars('wait_1')
            if lf_template('list'):
                moveTo(lf_template('list'))
                leftClick()
                wait_bars('wait_1')
                if lf_template('neot'):
                    moveTo(lf_template('neot'))
                    doubleClick()
                    wait_bars('wait_1')
                    if lf_template('yellow'):
                        change_row(lf_template('yellow'), 1)
                        wait_bars('wait_1')
                        press('pagedown')
                        wait_bars('wait_1')
                        moveTo(lf_template('save'))
                        leftClick()
                        wait_bars('wait_1')
                        leftClick()
                        wait_bars('wait_1')

    press('esc')
    wait_bars('wait_1')               







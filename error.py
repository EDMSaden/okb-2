from pyautogui import moveTo, leftClick, rightClick, doubleClick, press
from lf_template import lf_template
while True:
    if lf_template('error'):
        press('enter')
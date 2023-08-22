
from bars import lf_template,change_row,wait_bars, write_text, press_key, hot_key, leftClick, rightClick, doubleClick
from threading import Thread
from time import sleep


distance = 0
sleep(3)

def fix_error():
    count = 0
    while True:
        if lf_template('error'):
            press_key('enter')
            count += 1
            print(f'Недействующий характер заболевания: {count}')

th = Thread(target=fix_error, args=())
th.start()

while True:
    for i in range(12):
        if lf_template('start_1') and lf_template('start_2'):
            leftClick(55,446 + distance)
            distance += 30

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
                    press_key('pagedown')
                    wait_bars('wait_1')
                    leftClick(lf_template('save'))
                    wait_bars('wait_1')
                    wait_bars('wait_1')

        press_key('esc')
        wait_bars('wait_1')               
    
    if lf_template('ok'):
        leftClick(lf_template('ok'))
        distance = 0
        wait_bars('wait_1')  
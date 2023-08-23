
from bars import img_on_the_screen,change_row, write_text, press_key, hot_key, leftClickOn, rightClickOn, doubleClickOn, start_program
from time import sleep

sleep(3)

def program_1():
    while True:
        if img_on_the_screen('error'):
            press_key('enter')

def program_2():
    distance = 0
    while True:
        for i in range(12):
            if img_on_the_screen('start_1') and img_on_the_screen('start_2'):
                leftClickOn(55,446 + distance)
                distance += 30

                if img_on_the_screen('pos'):
                    change_row(986,245,'2')   
                    change_row(974,270,'2')
                    change_row(702,470,'6')
                    change_row(692,494,'1')
                    
                    if img_on_the_screen('result_1') and img_on_the_screen('result_2'):
                        press_key('pagedown')
                        leftClickOn('save')
                        leftClickOn('save')

            press_key('esc')

        if img_on_the_screen('ok'):
            leftClickOn(img_on_the_screen('ok'))
            distance = 0

start_program(program_1)
start_program(program_2)
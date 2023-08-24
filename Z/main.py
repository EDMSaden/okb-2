
from bars import img_on_the_screen,change_row, write_text, press_key, hot_key, leftClickOn, rightClickOn, doubleClickOn, start_program


def program_1():
    while True:
        if img_on_the_screen('error'):
            press_key('enter')


def program_2():
    distance = 0
    while True:
        for i in range(12):
            if img_on_the_screen('z1') and img_on_the_screen('purp1'):
                leftClickOn(31,450 + distance)
                distance += 33
                while True:
                    if img_on_the_screen('scrp1'):
                        #Цель
                        change_row(984,249,'профосмотр')
                        change_row(1007,268,'2 - Профилактическое')
                        change_row(739,471,'Осмотр')
                        change_row(697,495,'Лечение завершено')
                        if img_on_the_screen('rslt1') and img_on_the_screen('rslt2'):
                            press_key('pagedown')
                            leftClickOn('save')
                            leftClickOn('save')
                            if img_on_the_screen('purp2'):
                                leftClickOn('purp2')
                                press_key('pageup')
                            else:
                                press_key('pageup')
                                leftClickOn(648,171)
                                leftClickOn(858,778)
                                hot_key('ctrl', 'a')
                                press_key('backspace')
                                leftClickOn(1326,1006)
                                press_key('esc')
                                break
        distance = 0
        leftClickOn('ok')

start_program(program_1)
start_program(program_2)
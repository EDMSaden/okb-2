from bars import img_on_the_screen,change_row, write_text, press_key, hot_key, leftClickOn, rightClickOn, doubleClickOn, start_program, Exel
from time import sleep

exel = Exel(r'Ошибки_neZ.xlsx')

for i in range(1,193):
    if img_on_the_screen('start'):
        # № талона
        leftClickOn(331,228)
        hot_key('ctrl', 'a')
        write_text(exel.cell_value(i,1))
        # Дата с
        leftClickOn(926,253)
        hot_key('ctrl', 'a')
        write_text(exel.cell_value(i,7))
        # Дата по
        leftClickOn(938,275)
        hot_key('ctrl', 'a')
        write_text(exel.cell_value(i,7))

        press_key('enter')
        # Врач
        doubleClickOn(713,449)
        #Строка ниже нажимает ctrl + c и сверяет результат копирования со строкой из Exel
        if hot_key('ctrl', 'c') in exel.cell_value(i,5):
            leftClickOn(64,447)
            # Цель 
            change_row(965,247, '1')
            # Вид 
            change_row(971,271, '1')
            # Исход
            change_row(698,473, '3')
            # Результат 
            change_row(688,495, '1')
            if img_on_the_screen('res_1') and img_on_the_screen('res_2'):
                press_key('pagedown')
                leftClickOn('save')
                leftClickOn('save')
    press_key('esc')

            
    


          







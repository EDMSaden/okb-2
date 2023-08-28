from bars import img_on_the_screen,change_row, write_text, press_key, hot_key, leftClickOn, rightClickOn, doubleClickOn, start_program, Exel, send_message


exel = Exel('ОшибкиПнаЛ')

for i in range(2,93):
    if img_on_the_screen('start'):
        leftClickOn(330, 232)
        hot_key('ctrl', 'a')
        write_text(exel.cell_value(i,1))

        leftClickOn(949, 254)
        hot_key('ctrl', 'a')
        write_text(exel.cell_value(i,7))
        leftClickOn(958, 272)
        hot_key('ctrl', 'a')
        write_text(exel.cell_value(i,7))
        press_key('Enter')
        doubleClickOn(726, 450)
        if hot_key('ctrl','c') in exel.cell_value(i,5):
            leftClickOn(67, 447)
            change_row(1007, 271,'1 - По поводу заболевания')
            change_row(995, 247,'заболевание')
            change_row(710, 471,'Улучшение')
            change_row(720, 499,'Лечение завершено')
            if img_on_the_screen('prov1') and img_on_the_screen('prov2'):
                press_key('pagedown')
                leftClickOn('save')
                leftClickOn('save')
                press_key('esc')
                print(i)
        else:
            send_message(f'{i} - не пройдена')
    else:
        press_key('esc')
        send_message('Что то на экране')

send_message('Работа завершена')
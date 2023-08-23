from threading import Thread
import time


def start_program(program):
    th = Thread(target=program, args=())
    th.start()

def f1():
    while True:
        print('f1')
        time.sleep(1)

def f2():
    while True:
        print('f2')
        time.sleep(1)


start_program(f1)
start_program(f2)
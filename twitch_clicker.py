import pyautogui as pya
import time
import os
import sys

# variables
pya.FAILSAFE = False
p = (1667, 1011)
right_monitor = None


# functions
def display_position(interval: int = 1):
    while True:
        print(pya.position())
        time.sleep(interval)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_countdown(seconds: int, interval: int = 1):
    for i in range(seconds, 0, -1):
        print(f'Countdown: {str(i).rjust(2, " ")}', end='')
        time.sleep(interval)
        print('', end='\r')


def click_bonus_button(x: int, y: int, interval: int = 30):
    while True:
        last_position = pya.position()
        pya.click(x, y)
        print('Clicked the bonus button!')
        pya.moveTo(last_position.x, last_position.y)
        print(f'Moved back to {last_position}')
        display_countdown(interval)
        clear_console()


# main program
while right_monitor != 'true' and right_monitor != 'false':
    right_monitor = input(
        'Enter "True" to click on the right monitor or "False" to click on the left monitor: ').lower()
    if right_monitor != 'true' and right_monitor != 'false':
        print('Monitor toggle not set, try again.')
    else:
        if right_monitor == 'true':
            right_monitor = True
            print('Right monitor selected.')
        else:
            right_monitor = False
            print('Left monitor selected.')
        break

display_countdown(5)

if right_monitor:
    click_bonus_button(p[0], p[1])
else:
    click_bonus_button(p[0] - 1920, p[1])

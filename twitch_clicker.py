import pyautogui as pya
import time

pya.FAILSAFE = False

p = (1667, 1011)
u = (1789, 1011)

# while True:
#     print(pya.position())
#     time.sleep(1)

time.sleep(5)

while True:
    pya.click(p[0], p[1])
    pya.click(u[0], u[1])
    time.sleep(30)
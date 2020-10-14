import pyautogui as pya
import time

pya.FAILSAFE = False
p = (1667, 1011)
u = (1789, 1011)

rightMonitor = None
while rightMonitor != True and rightMonitor != False:
    rightMonitor = bool(input('Enter "True" or "False":'))
    if rightMonitor != True and rightMonitor != False:
        print('Monitor toggle not set, try again.')

# while True:
#     print(pya.position())
#     time.sleep(1)

time.sleep(5)
if rightMonitor:
    while True:
        pya.click(p[0], p[1])
        pya.click(u[0], u[1])
        time.sleep(30)
else:
    while True:
        pya.click(p[0] - 1920, p[1])
        pya.click(u[0] - 1920, u[1])
        time.sleep(30)

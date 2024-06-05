from pynput.mouse import Button, Controller as mouseController
from pynput.keyboard import Key, Controller as keyboardController
from time import sleep
from multiprocessing import Process
import pyautogui

pyautogui.alert(text='', title='', button='OK')
img1 = pyautogui.screenshot()
img1.save("c:/PlasticEater/screenshots/ip.png")

mouse = mouseController()
screenWidth, screenHeight = pyautogui.size()
pos = (screenWidth / 2, screenHeight / 2)
posCoord = str(pos).replace('(', '').replace(')', '').replace(' ', '').split(',')
posCoord[0] = int(posCoord[0])
posCoord[1] = int(posCoord[1])


def FixMouse():
    #shift + F5 to stop
    while mouse.position != pos or True:
        # sleep(0.001)
        tempPos = str(mouse.position).replace('(', '').replace(')', '').replace(' ', '').split(',')
        tempPos[0] = int(tempPos[0])
        tempPos[1] = int(tempPos[1])

        x = 0
        y = 0
        if tempPos[0] > posCoord[0]:
            x = -1
        elif tempPos[0] < posCoord[0]:
            x = 1
        if tempPos[1] > posCoord[1]:
            y = -1
        elif tempPos[1] < posCoord[1]:
            y = 1
        
        mouse.move(x ,y)

def runScript():
    keyboard = keyboardController()

    with keyboard.pressed(Key.cmd):
        keyboard.press('r')
        keyboard.release('r')
    sleep(0.5)
    keyboard.type('cmd')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.5)
    keyboard.type('cd c:/')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type('color 2')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.type('tree')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


#Execute Mutli task
if __name__ == "__main__":
    p1 = Process(target = FixMouse)
    p2 = Process(target = runScript)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
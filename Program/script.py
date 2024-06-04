from pynput.mouse import Button, Controller
from time import sleep

mouse = Controller()
pos = (176, 115)
posCoord = str(pos).replace('(', '').replace(')', '').replace(' ', '').split(',')
posCoord[0] = int(posCoord[0])
posCoord[1] = int(posCoord[1])

#shift + F5 to stop
while mouse.position != pos:
    sleep(0.001)
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
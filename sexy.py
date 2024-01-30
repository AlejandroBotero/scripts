import pyautogui as pg
from random import random
from time import sleep

pg.FAILSAFE = True

cs = (pg.size().width/2, pg.size().height/2)


lenrate = 0
while True:
    ranx = random()*lenrate
    rany = random()*lenrate
    if random() > 0.5:
        ranx = -ranx
    if random() > 0.5:
        rany = -rany
        
    pg.click(cs[0]+ranx, cs[1]+rany)
    pg.write('sexy')
    lenrate += 10
    sleep(0.001)

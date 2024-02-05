import keyboard
import pyautogui as pg


conf = {'px':100}

def move_x(pxtomv):
    pg.move(pxtomv, 0)
def move_y(pxtomv):
    pg.move(0, pxtomv)


def on_event(event):

    n= event.name

    #movement
    if n == 'h':
        move_x(-conf['px'])
    elif n == 'l':
        move_x(conf['px'])
    elif n == 'j':
        move_y(conf['px'])
    elif n == 'k':
        move_y(-conf['px'])
    
    #gear
    elif n == 'a':
        conf['px'] = 5
    elif n == 'o':
        conf['px'] = 35
    elif n == 'e':
        conf['px'] = 100
    elif n == 'u':
        conf['px'] = 200

    #events
    elif n == 't':
        pg.click()
    elif n == 'n':
        pg.click(button='right')
    elif n == 'b':
        pg.scroll(conf['px'])
    elif n == 'm':
        pg.scroll(-conf['px'])
   
    pg.write('/b')

keyboard.on_press(on_event)
keyboard.wait()

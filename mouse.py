import keyboard
import pyautogui as pg


px = 100

def move_x(pxtomv):
    pg.move(pxtomv, 0)
def move_y(pxtomv):
    pg.move(0, pxtomv)


def on_event(event):

    n= event.name
    if n == 'h':
        move_x(-px)
    elif n == 'l':
        move_x(px)
    elif n == 'j':
        move_y(px)
    elif n == 'k':
        move_y(-px)

keyboard.on_press(on_event)
keyboard.wait()

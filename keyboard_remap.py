import keyboard as kb
import pyautogui as pg

kb.add_hotkey('q', lambda: pg.write("'"), suppress=True)
kb.add_hotkey('w', lambda: pg.write(","), suppress=True)
kb.add_hotkey('e', lambda: pg.write('.'), suppress=True)
kb.add_hotkey('', lambda: pg.write(''), suppress=True)

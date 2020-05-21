import time
import pyautogui

def go(target):
    if target == 'battle':
        pyautogui.moveTo(1123, 1145, duration=-1000)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    if target == 'duel':
        pyautogui.moveTo(876, 1144, duration=-1000)

def pokemon_go(round, id):
    if round == 1:
        if id == 1:
            pyautogui.moveTo( 892, 1277, duration=-1000)
        elif id == 2:
            pyautogui.moveTo( 986, 1277, duration=-1000)
        elif id == 3:
            pyautogui.moveTo(1075, 1277, duration=-1000)
        elif id == 4:
            pyautogui.moveTo(1172, 1277, duration=-1000)
        elif id == 5:
            pyautogui.moveTo(1266, 1277, duration=-1000)
        elif id == 6:
            pyautogui.moveTo(1360, 1277, duration=-1000)
    if round == 2:
        if id == 1:
            pyautogui.moveTo( 941, 1277, duration=-1000)
        elif id == 2:
            pyautogui.moveTo(1031, 1277, duration=-1000)
        elif id == 3:
            pyautogui.moveTo(1123, 1277, duration=-1000)
        elif id == 4:
            pyautogui.moveTo(1217, 1277, duration=-1000)
        elif id == 5:
            pyautogui.moveTo(1313, 1277, duration=-1000)
    if round == 3:
        if id == 1:
            pyautogui.moveTo( 991, 1277, duration=-1000)
        elif id == 2:
            pyautogui.moveTo( 1079, 1277, duration=-1000)
        elif id == 3:
            pyautogui.moveTo(1177, 1277, duration=-1000)
        elif id == 4:
            pyautogui.moveTo(1269, 1277, duration=-1000)
    if round == 4:
        if id == 1:
            pyautogui.moveTo(1031, 1277, duration=-1000)
        elif id == 2:
            pyautogui.moveTo(1123, 1277, duration=-1000)
        elif id == 3:
            pyautogui.moveTo(1217, 1277, duration=-1000)
    if round == 5:
        if id == 1:
            pyautogui.moveTo( 1079, 1277, duration=-1000)
        elif id == 2:
            pyautogui.moveTo( 1177, 1277, duration=-1000)
    if round == 6:
        if id == 1:
            pyautogui.moveTo( 1075, 1277, duration=-1000)
    pyautogui.mouseDown()
    pyautogui.moveTo(1124, 1002, duration=-1000)
    pyautogui.mouseUp()

def battle():
    go('battle')
    time.sleep(15)
    pokemon_go(1,4)
    time.sleep(15)
    pokemon_go(2,1)
    time.sleep(15)
    pokemon_go(3,2)

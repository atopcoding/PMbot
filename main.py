import time
from variables import *
import pyautogui

def go(target):
    if target == 'battle':
        pyautogui.moveTo(1123, 1145, duration=-1000)
        pyautogui.click()
    elif target == 'duel':
        pyautogui.moveTo(876, 1144, duration=-1000)
    elif target == 'ad':
        pyautogui.moveTo(400, 840, duration=-1000)


def getBall(round, id):
    balls = 7 - round
    return (ballCtr + ballDist * (id - (balls + 1) / 2), ballY)

def pokemon_go(round, id):
    x, y = getBall(round, id)
    pyautogui.moveTo(x, y)
    pyautogui.drag(0, -100, button = 'left')

def battle():
    go('battle')
    time.sleep(20)
    print("Going to do move")
    pokemon_go(1,4)
    time.sleep(20)
    print("Going to do move")
    pokemon_go(2,3)
    print("Going to do move")
    time.sleep(20)
    pokemon_go(3,2)

import time
import pyautogui
import init

def go(target):
    if target == 'battle':
        pyautogui.moveTo(1127, 1156, duration=-1000)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    if target == 'duel':
        pyautogui.moveTo(876, 1144, duration=-1000)

def getBall(round, ball):
	ballnum = 7 - round
	return (1127 + (ball - (ballnum + 1) / 2) * 85, 1294)

def pokemon_go(r, b):
	x, y = getBall(r, b)
	pyautogui.moveTo(x, y)
	pyautogui.mouseDown()
	pyautogui.moveTo(1127, 1016, duration=-1000)
	pyautogui.mouseUp()

def battle():
    go('battle')
    time.sleep(20)
    pokemon_go(1, 4)
    time.sleep(20)
    pokemon_go(2, 1)
    time.sleep(20)
    pokemon_go(3, 2)
    time.sleep(20)
    pokemon_go(4, 3)
    time.sleep(20)
    pokemon_go(5, 2)

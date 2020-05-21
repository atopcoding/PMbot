import time
import pyautogui
import init

def go(target):
    if target == 'battle':
        pyautogui.moveTo(500, 780, duration=-1000)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    if target == 'duel':
        pyautogui.moveTo(876, 1144, duration=-1000)

def getBall(round, ball):
	ballnum = 7 - round
	return (500 + (ball - (ballnum + 1) / 2) * 60, 870)

def pokemon_go(r, b):
	x, y = getBall(r, b)
	pyautogui.moveTo(x, y)
	pyautogui.click()
	pyautogui.click()
	pyautogui.drag(0, -200, button='left')

def battle():
    init.screen_size()
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

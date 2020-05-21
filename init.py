import pyautogui

#Resize screen to fit 1000 * 1000
def screen_size():
	screenWidth, screenHeight = pyautogui.size()
	pyautogui.moveTo(screenWidth - 5, screenHeight - 5)
	pyautogui.click()
	pyautogui.dragTo(1000, 1000, button = 'left')

#center at x = 500, y = 870, width = 60
def getBall(round, ball):
	ballnum = 7 - round
	return (500 + (ball - (ballnum + 1) / 2) * 60, 870)

def go():
	r = int(input())
	b = int(input())
	x, y = getBall(r, b)
	pyautogui.moveTo(x, y)
	pyautogui.click()
	pyautogui.click()
	pyautogui.drag(0, -200, button = 'left')
	

import pyautogui

#Resize screen to fit 1000 * 1000
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth - 5, screenHeight - 5)
pyautogui.click()
pyautogui.dragTo(1000, 1000, button = 'left')

#center at x = 500, y = 870, width = 60
def getBall(round, ball):
	ballnum = 7 - round
	return (500 + (ball - (ballnum + 1) / 2) * 60, 870)



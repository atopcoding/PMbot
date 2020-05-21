import pyautogui
pyautogui.FAILSAFE = False

#Resize screen to fit 1000 * 1000
def screen_size():
	screenWidth, screenHeight = pyautogui.size()
	print(screenWidth, screenHeight)
	pyautogui.moveTo(screenWidth - 1, screenHeight - 1)
	pyautogui.click()
	pyautogui.dragTo(1000, 1000, button = 'left')

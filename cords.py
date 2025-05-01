import pyautogui 
import time

def take_cords():
    time.sleep(5)
    cords = pyautogui.position()
    print(cords)
take_cords()

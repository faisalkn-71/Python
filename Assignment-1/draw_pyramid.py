import pyautogui
import time

def draw_pyramid(height):
    for i in range(1, height + 1):
        pyautogui.typewrite('#' * i + '\n')
        time.sleep(0.1)  

height = int(input())

time.sleep(5)
draw_pyramid(height)



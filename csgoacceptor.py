#Author: Y3nlox 
#Add me on steam as 'Y3nlox'.
#You are welcome to donate a skins.
import  pyautogui
import time
import pynput

print(pyautogui.size())
print('Enter your in game resolution')
height = int(input('Enter the Height:  '))
width = int(input('Enter the Width:  '))


def AutoAccept():
    pyautogui.click(width/2,height/1.8)
    time.sleep(1.7)
    pyautogui.click(width/2.01,height/1.8)
    pass

while (True):
    AutoAccept()
    
    

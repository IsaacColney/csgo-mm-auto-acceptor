import  pyautogui
from twisted.internet import task, reactor
import pynput
from pynput import keyboard


print(pyautogui.size())
print('Enter your in game resolution')
height = int(input('Enter the Height:  '))
width = int(input('Enter the Width:  '))

timeout = 2


def doWork():
    pyautogui.click(width/2,height/1.8)
    timeout = 1
    pyautogui.click(width/2.01,height/1.8)
    pass


l = task.LoopingCall(doWork)
l.start(timeout)  #call every sixty seconds

reactor.run()



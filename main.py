import pyautogui
import os
from pynput.mouse import Listener
from pynput import keyboard
from time import sleep

positionList = []


def on_press(key):
    try:
        if key.char == 'x':
            os._exit(1)
    except AttributeError:
        pass


def on_click(x, y, button, pressed):
    if not pressed:
        return
    if len(positionList) < 3:
        positionList.append((x, y))


def get_position_list():
    print("Manually disenchant a champion")
    listener = Listener(on_click=on_click)
    listener.start()
    while len(positionList) < 3:
        sleep(0.2)
    listener.stop()


def disenchant_champions():
    q = 2000
    print("disenchanting")
    print("press 'x' to stop")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while q > 0:
        q -= 1
        for position in positionList:
            pyautogui.moveTo(x=position[0], y=position[1], duration=0.5, tween=pyautogui.easeInQuad)
            sleep(0.8)
            pyautogui.leftClick()
    listener.stop()


def test_keyboard():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    q = 0
    while q < 10:
        q += 1
        sleep(1)
        print(q)
    listener.stop()


if __name__ == '__main__':
    get_position_list()
    disenchant_champions()

import keyboard
import pyautogui
import win32api
import win32con

from pyautogui import *

# images
referenceFolder = 'screenshots\\'
award = referenceFolder + 'award.png'
threeHundred = referenceFolder + '300.png'
giveAward = referenceFolder + 'give_award.png'
next = referenceFolder + 'next.png'
award2 = referenceFolder + 'award2.png'

# buttons
defaultPos = (-100, -100)
awardButton, threeHundredButton, giveAwardButton, nextButton = defaultPos, defaultPos, defaultPos, defaultPos

def moveCursor(position: Point):
    win32api.SetCursorPos(position)


def leftMouseDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)


def leftMouseUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def click(x, y):
    moveCursor((x, y))
    leftMouseDown()
    time.sleep(0.1)
    leftMouseUp()


def clickAndReset(x, y):
    previousX, previousY = win32api.GetCursorPos()
    click(x, y)
    moveCursor((previousX, previousY))


def giveAwards():
    while True:
        try:
            awardButton = pyautogui.locateCenterOnScreen(award, grayscale=True, confidence=0.8)
            if awardButton is None:
                awardButton = pyautogui.locateCenterOnScreen(award2, grayscale=True, confidence=0.8)
            clickAndReset(awardButton.x, awardButton.y)
            time.sleep(2)

            threeHundredButton = pyautogui.locateCenterOnScreen(threeHundred, grayscale=False, confidence=0.99)
            if threeHundredButton is None:
                print('no more awards to give')
                return

            clickAndReset(threeHundredButton.x, threeHundredButton.y)
            time.sleep(2)

            giveAwardButton = pyautogui.locateCenterOnScreen(giveAward, grayscale=True, confidence=0.8)
            clickAndReset(giveAwardButton.x, giveAwardButton.y)
            time.sleep(2)

            nextButton = pyautogui.locateCenterOnScreen(next, grayscale=True, confidence=0.8)
            clickAndReset(nextButton.x, nextButton.y)
            time.sleep(5)

        except ImageNotFoundException:
            print('no more awards to give')
            return


if __name__ == '__main__':
    print('award giving program has started')
    while not keyboard.is_pressed('esc'):
        if keyboard.is_pressed('space'):
            print('starting giving awards')
            giveAwards()

        time.sleep(0.01)

import pyautogui
import time
import pyperclip

while True:
    pyautogui.click(1185, 1066)
    time.sleep(1)

    pyautogui.moveTo(333, 153)
    pyautogui.dragTo(1660, 950, duration=1.0, button='left')

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(1660, 950)
    text = pyperclip.paste()

    print(text)
    break
    # print(a)
    # 360,133, 1821,968

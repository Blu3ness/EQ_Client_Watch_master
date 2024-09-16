import pyautogui
import keyboard
import time

import functions

pizza = ''

def error_window_detection(): #looks for client error window


    error_windows = pyautogui.locateAllOnScreen("error.png", confidence=0.9)

    if error_windows:
        # Multiple error windows found
        for error_window in error_windows:
            # Handle each error window individually
            functions.kill_all()  # Adjust or replace with specific action
            print(f"Error window detected at: {error_window}")


def eula_button_finder():
    x, y = pyautogui.locateCenterOnScreen("eula_accept_button.png", confidence= 0.9)
    pyautogui.moveTo(x,y, duration=0.3)
    click()
    click()
    print(x,y)
    # login()


# def login():
#     x, y = pyautogui.locateCenterOnScreen("eula_accept_button.png", confidence= 0.9)
#     pyautogui.moveTo(x,y, duration=1)
#     click()
#     click()
#
#     time.sleep(1)

    keyboard.press_and_release('enter')
    x, y = pyautogui.locateCenterOnScreen("login_login_button.png", confidence= 0.5)
    print("Login button at: ", x,y)

    type_it(pizza)


    pyautogui.moveTo(x,y, duration=0.3)
    click()

    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(20)

    keyboard.press_and_release('enter')

    time.sleep(2)
    print("Blue Logged In!")
    # keyboard.press_and_release('enter')

    # qx, qy = pyautogui.locateCenterOnScreen("quick_connect.png", confidence= 0.8)
    # pyautogui.moveTo(qx,qy)
    # click()
    # pyautogui.click(x, y)
    # # pyautogui.moveTo(x,y, duration=1)
    # print('button click login')
    # # pyautogui.press('enter')


    # mouse.click(Button.left)
    # click()

def click():
    pyautogui.mouseDown()
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.mouseUp()


def type_it(text):

    for letter in text:
        if letter.isupper():
            keyboard.send("shift+" + letter)
        else:
            keyboard.write(letter, exact=False)
        time.sleep(0.02)

    # for letter in the_text:
    #     if letter.isupper():
    #         keyboard.send("shift+" + letter)
    #
    #     else:
    #         print(pizza)
    #
    #         # keyboard.write(letter, exact=False)
    #     time.sleep(0.02)

# import cv2
# import numpy as np
# import pyautogui
# import time
# from pynput.mouse import Button, Controller
# from pynput.keyboard import Controller as KB
#
# mouse = Controller()
# keyboard = KB
#
# accept_button_x = 972
# accept_button_y = 666
#
# login_button_x = 900
# login_button_y = 420
#
# current_x, current_y = pyautogui.position()
#
# # Define the number of steps for smoother movement
# steps = 20  # You can adjust this value for more or less granularity
#
# # Calculate the step size for each coordinate
# step_x = (accept_button_x - current_x) / steps
# step_y = (accept_button_y - current_y) / steps
#
#
# def click_it():
#     for i in range(steps):
#         pyautogui.moveTo(current_x + (i * step_x), current_y + (i * step_y))
#         time.sleep(0.005)
#
#     pyautogui.moveTo(accept_button_x,accept_button_y)
#     mouse.click(Button.left)
#     time.sleep(.5)
#     mouse.click(Button.left)
#     print("Click sent")
#     time.sleep(1)
#     pyautogui.moveTo(login_button_x, login_button_y)
#     mouse.click(Button.left)
#
#     time.sleep(1)
#     pyautogui.typewrite("Hello")

# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
import threading

STEPPERREV = 512

enable_pin = digitalio.DigitalInOut(board.D19)
coil_A_1_pin = digitalio.DigitalInOut(board.D4)
coil_A_2_pin = digitalio.DigitalInOut(board.D17)
coil_B_1_pin = digitalio.DigitalInOut(board.D23)
coil_B_2_pin = digitalio.DigitalInOut(board.D24)

enable_pin.direction = digitalio.Direction.OUTPUT
coil_A_1_pin.direction = digitalio.Direction.OUTPUT
coil_A_2_pin.direction = digitalio.Direction.OUTPUT
coil_B_1_pin.direction = digitalio.Direction.OUTPUT
coil_B_2_pin.direction = digitalio.Direction.OUTPUT

enable_pin = digitalio.DigitalInOut(board.D18)
coil_C_1_pin = digitalio.DigitalInOut(board.D22)
coil_C_2_pin = digitalio.DigitalInOut(board.D16)
coil_D_1_pin = digitalio.DigitalInOut(board.D25)
coil_D_2_pin = digitalio.DigitalInOut(board.D27)

enable_pin.direction = digitalio.Direction.OUTPUT
coil_C_1_pin.direction = digitalio.Direction.OUTPUT
coil_C_2_pin.direction = digitalio.Direction.OUTPUT
coil_D_1_pin.direction = digitalio.Direction.OUTPUT
coil_D_2_pin.direction = digitalio.Direction.OUTPUT

enable_pin.value = True

####### Right side
def forwardR(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepR(1, 0, 1, 0)
        time.sleep(delay)
        setStepR(0, 1, 1, 0)
        time.sleep(delay)
        setStepR(0, 1, 0, 1)
        time.sleep(delay)
        setStepR(1, 0, 0, 1)
        time.sleep(delay)
        i += 1

def backwardsR(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepR(1, 0, 0, 1)
        time.sleep(delay)
        setStepR(0, 1, 0, 1)
        time.sleep(delay)
        setStepR(0, 1, 1, 0)
        time.sleep(delay)
        setStepR(1, 0, 1, 0)
        time.sleep(delay)
        i += 1

def setStepR(w1, w2, w3, w4):
    coil_A_1_pin.value = w1
    coil_A_2_pin.value = w2
    coil_B_1_pin.value = w3
    coil_B_2_pin.value = w4

###### left side

def forwardL(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepL(1, 0, 1, 0)
        time.sleep(delay)
        setStepL(0, 1, 1, 0)
        time.sleep(delay)
        setStepL(0, 1, 0, 1)
        time.sleep(delay)
        setStepL(1, 0, 0, 1)
        time.sleep(delay)
        i += 1

def backwardsL(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepL(1, 0, 0, 1)
        time.sleep(delay)
        setStepL(0, 1, 0, 1)
        time.sleep(delay)
        setStepL(0, 1, 1, 0)
        time.sleep(delay)
        setStepL(1, 0, 1, 0)
        time.sleep(delay)
        i += 1

def setStepL(w1, w2, w3, w4):
    coil_C_1_pin.value = w1
    coil_C_2_pin.value = w2
    coil_D_1_pin.value = w3
    coil_D_2_pin.value = w4

def goForward(steps):
    fx = threading.Thread(target=forwardR, args= (int(user_delay)/1000.0,int(steps)))
    fy = threading.Thread(target=forwardL, args= (int(user_delay)/1000.0,int(steps)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()

def goBackward(steps):
    fx = threading.Thread(target=backwardsR, args= (int(user_delay)/1000.0,int(steps)))
    fy = threading.Thread(target=backwardsL, args= (int(user_delay)/1000.0,int(steps)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()

def turnRight(degrees):
    steps = degrees/360.0 * STEPPERREV
    fx = threading.Thread(target=backwardsR, args= (int(2)/1000.0,int(steps)))
    fy = threading.Thread(target=forwardL, args= (int(user_delay)/1000.0,int(steps)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()

def turnLeft(degrees):
    steps = degrees/360.0 * STEPPERREV
    fx = threading.Thread(target=backwardsL, args= (int(user_delay)/1000.0,int(steps)))
    fy = threading.Thread(target=forwardR, args= (int(user_delay)/1000.0,int(steps)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()

while True:
    user_delay = input("Delay between steps (milliseconds)?")
    user_steps = input("How many steps forward? Right wheel")

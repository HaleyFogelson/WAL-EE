import time
from turtle import forward
import board
import digitalio
import threading
import math
import csv

STEPPERREV = 512
SCALEFACTOR = 2
WIDTHROBOT = 12
WHEELDIAM = 2.4

coil_A_1_pin = digitalio.DigitalInOut(board.D4)
coil_A_2_pin = digitalio.DigitalInOut(board.D27)
coil_B_1_pin = digitalio.DigitalInOut(board.D22)
coil_B_2_pin = digitalio.DigitalInOut(board.D23)

coil_A_1_pin.direction = digitalio.Direction.OUTPUT
coil_A_2_pin.direction = digitalio.Direction.OUTPUT
coil_B_1_pin.direction = digitalio.Direction.OUTPUT
coil_B_2_pin.direction = digitalio.Direction.OUTPUT




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


forwardR(.02,1000)

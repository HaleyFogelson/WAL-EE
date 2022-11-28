# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
from turtle import forward
import board
import digitalio
import threading
import math
import csv
import pigpio
from gpiozero import Servo

STEPPERREV = 512
SCALEFACTOR = 10
user_delay=2
RADWHEEL = 3.5
ROBOTWIDTH=28.5
timeMax = .002
timeRatio = .01#21.5/8.3 * timeMax * 2 #right wheel from actuator/ left wheel wheel actuator * 2 Max
leftTicksPerRad = 663.87
rightTicksPerRad = 139.739
print("The time ratio is: ", timeRatio)


coil_A_1_pin = digitalio.DigitalInOut(board.D4)
coil_A_2_pin = digitalio.DigitalInOut(board.D17)
coil_B_1_pin = digitalio.DigitalInOut(board.D23)
coil_B_2_pin = digitalio.DigitalInOut(board.D24)

coil_A_1_pin.direction = digitalio.Direction.OUTPUT
coil_A_2_pin.direction = digitalio.Direction.OUTPUT
coil_B_1_pin.direction = digitalio.Direction.OUTPUT
coil_B_2_pin.direction = digitalio.Direction.OUTPUT

coil_C_1_pin = digitalio.DigitalInOut(board.D22)
coil_C_2_pin = digitalio.DigitalInOut(board.D16)
coil_D_1_pin = digitalio.DigitalInOut(board.D25)
coil_D_2_pin = digitalio.DigitalInOut(board.D27)


coil_C_1_pin.direction = digitalio.Direction.OUTPUT
coil_C_2_pin.direction = digitalio.Direction.OUTPUT
coil_D_1_pin.direction = digitalio.Direction.OUTPUT
coil_D_2_pin.direction = digitalio.Direction.OUTPUT

servo = Servo(13)# this is the actuator
"""
servo = pigpio.pi()
servoPin = 13
servo.set_mode(servoPin,pigpio.OUTPUT)
servo.set_PWM_frequency(servoPin, 50)
"""

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

def backwardsL(delay, steps):
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

def forwardL(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepL(1, 0, 0, 1)
        time.sleep(delay)
        setStepL(0, 1, 1, 0)
        time.sleep(delay)
        setStepL(0, 1, 0, 1)
        time.sleep(delay)
        setStepL(1, 0, 0, 1)
        time.sleep(delay)
        i += 1

def forwardL(delay, steps):
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
    print("going foward steps:",steps)
    fx = threading.Thread(target=forwardR, args= (.003,int(steps)))
    fy = threading.Thread(target=backwardsL, args= (.003,int(steps)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()

def goBackward(steps):
    fx = threading.Thread(target=backwardsR, args= (.002,int(steps)))
    fy = threading.Thread(target=backwardsL, args= (.002, int(steps)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()

def turnLeft(rad):
    numRev= ROBOTWIDTH / (RADWHEEL*2*3.14)
    steps = rad/(2*3.14) * STEPPERREV * numRev
    #3684 left for 2pi rad
    #760 rigth for 2i rad
    turnsLeft = leftTicksPerRad * rad
    turnsRight = rightTicksPerRad * rad
    print("TURN LEFTTTTTTTT")
    fx = threading.Thread(target=backwardsR, args= (timeMax,int(turnsLeft)))
    fy = threading.Thread(target=backwardsL, args= (timeRatio,int(turnsRight)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()
    #time.sleep(timeMax*turnsLeft)
    print("Turned left")

def turnRight(rad):
    numRev= ROBOTWIDTH / (RADWHEEL*2*3.14)
    steps = rad/(2*3.14) * STEPPERREV * numRev
    print("TURN RIGHHTTTTTTTT")
    #3684 left for 2pi rad
    #760 rigth for 2i rad
    turnsLeft = leftTicksPerRad * rad
    turnsRight = rightTicksPerRad * rad

    fx = threading.Thread(target=forwardR, args= (timeMax,int(turnsLeft)))
    fy = threading.Thread(target=forwardL, args= (timeRatio,int(turnsRight)))
    fx.start()
    fy.start()
    fx.join()
    fy.join()
    #time.sleep(timeMax*turnsLeft)
    #print("turned right")

def move(prevRad, xStep, yStep):
    #diameter = 2.5 inches
    #circumference = 7.85 inches
    #2048 steps
    #512 in one rotation
    #4 ticks * SCALEFACTOR in 1 pixel
    stepsPerRevolution = 512
    #print("XSTEP:")
    print(xStep)
    #print("YSTEP:")
    print(yStep)

    length = math.sqrt(pow(xStep,2) + pow(yStep,2))
    rad_calc = math.atan2(yStep,xStep) #degrees between 2 pixels

    print("RADIAN CALUCLATED: " + str(rad_calc))
    #angletoMove = currAngle + degrees
    #angleToSteps = angletoMove/360 * stepsPerRevolution

    rad = rad_calc - prevRad

    print("RADIAN AFTERRRRRRRRRRR: ")
    print(rad)

    if rad > 0:
        if rad<3.14:
            turnLeft(rad)
        else:
            turnRight((rad-6.28)*-1)
        time.sleep(timeMax*rad*leftTicksPerRad)
    elif rad < 0:
        if rad>-3.14:
            turnRight(rad*-1)
        else:
            turnLeft((rad+6.28))
        time.sleep(timeMax*rad*leftTicksPerRad*-1)

    #going straight after angling
    goForward(4*SCALEFACTOR*length)
    prevRad = rad_calc
    return prevRad

def movePenDown(): #turn off LED
  #pull pen up
  #print("moving pen up")
    servo.mid()
    time.sleep(1) #pause for 3 seconds

def movePenUp(): #turn on LED
  #push pen up
  #print("moving pen down")
    servo.min()
    time.sleep(1) #pause for 3 seconds

def readCSV():
    with open('/home/pi/programs/NEU') as csvfile:
        data = [(float(x), float(y)) for x, y in csv.reader(csvfile, delimiter= ',')]
    print(data)
    #print("read in csv")
    return data

#1. read in cvs coordinates
#2.

def loop():
    drawing = True
    prevRad = 0
    while drawing:
        time.sleep(.1)
        coordinates = readCSV();
        numCoords = len(coordinates) #reads total number of coordinates

        movePenUp() #initializes pen as up
        xOld = 0 #initializes, axis start at (0.0)
        yOld = 0
        #print("made it thru csv")

        for i in range(0,numCoords):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            #python sends in next two coords
            coordX, coordY = coordinates[i] #reads x and y
            print("(" , coordX, " ," , coordY , ")")
            #print(coordX)
            #print(coordY)

            #calculate difference
            xStep = coordX - xOld
            yStep = coordY - yOld


            if ((abs(xStep) > 5) or (abs(yStep) > 5)): #pixels too far apart, lift up pen and move
                movePenUp()
                prevRad = move(prevRad, xStep, yStep)
                print("PREVIOUS RAD: " + str(prevRad))
                movePenDown()
            else:
                movePenDown()
                prevRad = move(prevRad, xStep, yStep)
                print("PREVIOUS RAD: " + str(prevRad))

            xOld = coordX
            yOld = coordY

        #movePenUp()
        drawing = False #stop drawing when image is complete

#movePenUp()
#movePenDown()
#goForward(1000)
#turnLeft(3.14)
#time.sleep(1)
# turnRight(1.57)
# time.sleep(3)
# turnLeft(1.57)
loop()



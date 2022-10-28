from time import sleep
import board
import digitalio
import RPi.GPIO as GPIO

MotorEnableR = 18
MotorAR = 4
MotorBR = 17
MotorCR = 23
MotorDR = 24

#Fix this
MotorEnableL = 19
MotorAL = 22
MotorBL = 16
MotorCL = 25
MotorDL = 27


def setUp():
    #set up right wheel
    GPIO.setup(MotorEnableR, GPIO.OUT)
    GPIO.setup(MotorAR, GPIO.OUT)
    GPIO.setup(MotorBR, GPIO.OUT)
    GPIO.setup(MotorCR, GPIO.OUT)
    GPIO.setup(MotorDR, GPIO.OUT)
    GPIO.output(MotorEnableR, GPIO.HIGH)

    #set up left wheel
    GPIO.setup(MotorEnableL, GPIO.OUT)
    GPIO.setup(MotorAL, GPIO.OUT)
    GPIO.setup(MotorBL, GPIO.OUT)
    GPIO.setup(MotorCL, GPIO.OUT)
    GPIO.setup(MotorDL, GPIO.OUT)
    GPIO.output(MotorEnableL, GPIO.HIGH)


# right wheel
def forwardR(delay, steps):
    i = 0
    while i in range(1, steps):
        setStepR(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        setStepR(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        setStepR(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        sleep(delay)
        setStepR(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        sleep(delay)
        i += 1

def forwardR2(delay, steps):
    i = 1
    while i in range(1, steps+1):
        if(i%4==0):
            setStepR(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        elif(i%3==0):
            setStepR(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        elif(i%2==0):
            setStepR(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        else:
            setStepR(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        i += 1

def backwardsR(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepR(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        sleep(delay)
        setStepR(0, GPIO.HIGH, 0,GPIO.HIGH)
        sleep(delay)
        setStepR(0, GPIO.HIGH, GPIO.HIGH, 0)
        sleep(delay)
        setStepR(GPIO.HIGH, 0, GPIO.HIGH, 0)
        sleep(delay)
        i += 1

def setStepR(w1, w2, w3, w4):
    GPIO.output(MotorAR, w1)
    GPIO.output(MotorBR, w2)
    GPIO.output(MotorCR, w3)
    GPIO.output(MotorDR, w4)

################################### Left wheel ##################################
def forwardL(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepL(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        setStepL(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        setStepL(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
        sleep(delay)
        setStepL(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        sleep(delay)
        i += 1

def backwardsL(delay, steps):
    i = 0
    while i in range(0, steps):
        setStepR(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        sleep(delay)
        setStepR(GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.HIGH)
        sleep(delay)
        setStepR(0, GPIO.HIGH, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        setStepR(GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        sleep(delay)
        i += 1

def setStepL(w1, w2, w3, w4):
    GPIO.output(MotorAL, w1)
    GPIO.output(MotorBL, w2)
    GPIO.output(MotorCL, w3)
    GPIO.output(MotorDL, w4)


while True:
    user_delay = input("Delay between steps (milliseconds)?")
    user_steps = input("How many steps forward? ")
    forwardR(int(user_delay) / 1000.0, int(user_steps))
    user_steps = input("How many steps backwards? ")
    backwardsR(int(user_delay) / 1000.0, int(user_steps))
#include <Stepper.h>
#include <Servo.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

import csv
import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 22
Motor1B = 27
Motor1E = 17

Motor2A = 4;
Motor2B = 23;
Motor2C = 25;

#STEPSPERREV = 20
#servoPin = 6

#Hardware Initialization
#Servo penServo#initiates servo
#Stepper xAxis(STEPSPERREV, 2, 3, 10, 11) #pins x axis motor are connected to
#Stepper yAxis(STEPSPERREV, 4, 5, 8, 9) #pins y axis motor are connected to

#Dynamic Memory Initialization
drawing = true
xStep = 0
yStep = 0
xOld = 0
yOld = 0
coordX = 0
coordY = 0

#Function Declarations
# def movePenUp()
# def movePenDown()
# def drawX(n)
# def drawY(n)
# def blockingRead()
# def convertSerialInputStringToInt()

def setup():
  GPIO.setmode(GPIO.BCM)        # GPIO Numbering
  GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
  GPIO.setup(Motor1B,GPIO.OUT)
  GPIO.setup(Motor1E,GPIO.OUT)


def loop():
    drawing = True
    while drawing:
        time.sleep(6)
        numCoords = blockingRead() #reads total number of coordinates
    
        movePenUp() #initializes pen as up
        xOld = 0 #initializes, axis start at (0.0)
        yOld = 0

        for i in numCoords:
          print("\n")
          print("@GetNext") #gives order to imageProcessing.py
          sleep(3000)

          #python sends in next two coords
          coordX = blockingRead() #reads x
          coordY = blockingRead() #reads y

          #calculate difference
          xStep = coordX - xOld
          yStep = coordY - yOld

          if ((abs(xStep) > 5) or (abs(yStep) > 5)): #pixels too far apart, lift up pen and move
            #movePenUp()
              drawX(xStep)
              drawY(yStep)
              #movePenDown()
          
          else: #draws
            drawX(xStep)
            drawY(yStep)

          xOld = coordX
          yOld = coordY

        #movePenUp()
    drawing = false #stop drawing when image is complete

#Here we have all the helper functions

def movePenUp(): #turn off LED
  #penServo.write(70)#pulls pen up
  print("moving pen up")
  sleep(1000) #pause for 3 seconds

def movePenDown(): #turn on LED
  #penServo.write(0)#pulls pen up
  print("moving pen down")
  sleep(1000) #pause for 3 seconds



#function for drawing x
def drawX(stepsToMove):
  steps = 0
  if (stepsToMove > 0): #to move forwards
    steps = 1
  else: #to move backwards
    stepsToMove *= -1
    steps = -1
  for x in range(stepsToMove):
    #xAxis.step(steps)
    sleep(10)


#function for drawing y
def drawY(stepsToMove):
  print("drawing y direction")
  steps = 0
  if (stepsToMove > 0): #to move forwards
    steps = 1
  else: #to move backwards
    stepsToMove *= -1
    steps = -1

  for x in range(stepsToMove):
    yAxis.step(steps)
    sleep(10)

"""
def blockingRead(): #buffers before reading to make sure serial input is fully sent
  while (!Serial.available())
  {
    delay(100)
  }
  return convertSerialInputStringToInt()


def convertSerialInputStringToInt(): #convert csv to int#
    with open("random.csv", newline = "") as f:
        csvreader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC, delimiter = ',') 
        output = []
        for row in csvreader: 
            output.append(row[:])

        for rows in outpugt:
            print(rows)


  #only called when serial is available
  String resultStr
  int resultInt
  String inputString = ""
  char tempChar = Serial.read()

  #reads entire input char by char into a string
  while tempChar is not ' ' and tempChar is not '\n' # python inputs coordinates seperated by spaces and new lines
  {
    inputString += (char)tempChar
    tempChar = Serial.read()
    delay(100)
  }

  #parses that string into an int
  len = inputString.length()
  for i in len:
    if (inputString[i] == '.') #python sends string with number that looks like a float, 
    {                         #end parsing when reaching the decimal because we just want the integer part
      break
    }
    else if (inputString[i] >= 48 and inputString[i] <= 57) #is an integer 0 to 9 
    {
      resultStr += inputString[i]
    }
  resultInt = resultStr.toInt()

  return resultInt

  """
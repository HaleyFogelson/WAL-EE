#include <Stepper.h>
#include <Servo.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

import time
import csv

const int stepsPerRevolution = 20
const int servoPin = 6

#Hardware Initialization
Servo penServo#initiates servo
Stepper xAxis(stepsPerRevolution, 2, 3, 10, 11) #pins x axis motor are connected to
Stepper yAxis(stepsPerRevolution, 4, 5, 8, 9) #pins y axis motor are connected to

#Dynamic Memory Initialization
bool drawing = true
int xStep
int yStep
int xOld
int yOld
int coordX
int coordY

#Function Declarations
void movePenUp()
void movePenDown()
void drawX(int n)
void drawY(int n)
int blockingRead()
int convertSerialInputStringToInt()

void setup()
{
  xAxis.setSpeed(100)
  yAxis.setSpeed(100)
  penServo.attach(servoPin)
  Serial.begin(9600)
}

def loop():
    drawing = True
    while drawing:
        time.sleep(6)
        int numCoords = blockingRead() #reads total number of coordinates
    
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

        if ((abs(xStep) > 5) or (abs(yStep) > 5)) #pixels too far apart, lift up pen and move
        {
            #movePenUp()
            drawX((int)xStep)
            drawY((int)yStep)
            #movePenDown()
        }
        else #draws
        {
            drawX((int)xStep)
            drawY((int)yStep)
        }
        xOld = coordX
        yOld = coordY
        #movePenUp()
    drawing = false #stop drawing when image is complete

"""
void movePenUp() #turn off LED
{
  penServo.write(70)#pulls pen up
  delay(1000) #pause for 3 seconds
}

void movePenDown() #turn on LED
{
  penServo.write(0)#pulls pen up
  delay(1000) #pause for 3 seconds
}
"""

"""
void drawX(int stepsToMove)
{
  int steps
  if (stepsToMove > 0) #to move forwards
  {
    steps = 1
  }
  else #to move backwards
  {
    stepsToMove *= -1
    steps = -1
  }
  for (int i = 0 i < (int)stepsToMove i++)
  {
    xAxis.step(steps)
    delay(10)
  }
}

void drawY(int stepsToMove)
{
  int steps
  if (stepsToMove > 0) #to move forwards
  {
    steps = 1
  }
  else #to move backwards
  {
    stepsToMove *= -1
    steps = -1
  }
  for (int i = 0 i < (int)stepsToMove i++)
  {
    yAxis.step(steps)
    delay(10)
  }
}

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
  int len = inputString.length()
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
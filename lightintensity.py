import RPi.GPIO as GPIO #import the libraries
import time
import os
GPIO.setmode(GPIO.BCM)  #setting up the numbering plan (BCM or BOARD)
GPIO.setwarnings(False)
def RCtime (RCpin):
    reading=0
    GPIO.setup(RCpin,GPIO.OUT)  #make GPIO18 as the output pin, and make it as low, capacitar has both the ends zero.
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(0.1)   #give a time delay
    GPIO.setup(RCpin,GPIO.IN)
    while (GPIO.input(RCpin)==GPIO.LOW):
        reading+=1                        #make the gpio 18 as the input pin, capacitor charges, it measures the time it take to reach high.
        return reading
light=RCtime(18)
while True:
    print (light)
    
        

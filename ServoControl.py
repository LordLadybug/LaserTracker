#Example (partially) directly copied from tutorial-- not final version

import RPi.GPIO as GPIO
import time

def ServoSetup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

def ServoStart(servoPIN):
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization
    return p

def Swivel(p):
    k=0
    try:
        while k<10:
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            k+=1
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

def CorrectCameraPosition(p, HorizontalError):
    ErrorToDutyCycle = 2.5/HorizontalError #replace with proper formula
    p.ChangeDutyCycle(ErrorToDutyCycle)


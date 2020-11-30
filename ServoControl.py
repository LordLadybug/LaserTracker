#Example (partially) directly copied from tutorial-- not final version

import RPi.GPIO as GPIO
import time

MaxDutyCycle = 10   #specific to the servos being used; highest position is 10% duty cycle at 50 hz
MinDutyCycle = MaxDutyCycle/4	#specific to the servos being used, 2.5% being the lowest position

def ServoSetup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

def ServoStart(servoPIN):
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(MaxDutyCycle/2) # Initialization
    return p

def Swivel(p):
    k=0
    try:
	#per the datasheet, 5-10% covers the whole range of motion
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
    ErrorToDutyCycle = MaxDutyCycle*HorizontalError #replace with proper formula
    p.ChangeDutyCycle(ErrorToDutyCycle)


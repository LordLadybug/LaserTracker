#Example (partially) directly copied from tutorial-- not final version

import RPi.GPIO as GPIO
import time

class ServoAngle():
    MaxDutyCycle = 100
    MinDutyCycle = 0	#defaults to these unless otherwise specified
	MinAngle = 0
	MaxAngle = 180		#maximum angle for a typical servo in degrees

    def AngleToDutyCycle(self, Angle):
        return (MaxDutyCycle-MinDutyCycle) * (MaxAngle-Angle) / (MaxAngle-MinAngle)

    def DutyCycleToAngle(self, DutyCycle):
        return (MaxAngle-MinAngle) * (MaxDutyCycle - DutyCycle) / (MaxDutyCycle - MinDutyCycle)

    def DutyCycleLimits():
        input(self.MinDutyCycle, "What is the minimum duty cycle?")
        input(self.MaxDutyCycle, "What is the maximum duty cycle?")

MaxDutyCycle = 10   #specific to the servos being used; highest position is 10% duty cycle at 50 hz
MinDutyCycle = MaxDutyCycle/4	#specific to the servos being used, 2.5% being the lowest position
#should create a data structure for specifying angle and defining its bounds to the max and min duty
#cycle
#Note: no change in angles specified here for our particular servos

def ServoSetup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

def ServoStart(servoPIN):
    ServoSetup(servoPIN)
    pwm = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    pwm.start(MaxDutyCycle/2) # Initialization
    return pwm

def Swivel(pwm):
    k=0
    try:
	#per the datasheet, 5-10% covers the whole range of motion, should hardcode these limits or
	#write in a way to configure servo characteristics into this code
        while k<10:
            pwm.ChangeDutyCycle(5)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(10)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(12.5)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(10)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(7.5)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(5)
            time.sleep(0.5)
            pwm.ChangeDutyCycle(2.5)
            time.sleep(0.5)
            k+=1
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
    pwm.stop()
    GPIO.cleanup()

def CorrectCameraPosition(pwm, HorizontalError):
    ErrorToDutyCycle = (MaxDutyCycle-MinDutyCycle)*HorizontalError/2 + (MaxDutyCycle+MinDutyCycle)/2
    pwm.ChangeDutyCycle(ErrorToDutyCycle)

def SwivelToAngle(Angle, pwm):
    pwm.ChangeDutyCycle(AngletoDutyCycle(Angle))

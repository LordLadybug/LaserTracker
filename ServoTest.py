import ServoControl
import RPi.GPIO as GPIO
import time


def Swivel(pwm):
    k=0
    #per the datasheet, 5-10% covers the whole range of motion, should hardcode these limits
    #  or write in a way to configure servo characteristics into this code
    while k<10:
        pwm.ChangeDutyCycle(5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(5)
        time.sleep(0.5)
        time.sleep(0.5)
        k+=1


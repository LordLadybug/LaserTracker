import RPi.GPIO as GPIO
import time
class Servo():
    def __init__(self, servopin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servopin, GPIO.OUT)
        self.pwm = GPIO.PWM(servopin, 50) # GPIO 17 for PWM with 50Hz
        self.pwm.start(5) # Initialization

    def Teardown(self):
        self.pwm.stop()
        GPIO.cleanup()

    class ServoAngle():
        MaxDutyCycle = 10   #specific to the servos being used; highest position is 10% duty cycle at 50 hz
        MinDutyCycle = MaxDutyCycle/4	#specific to the servos being used, 2.5% being the lowest position
        #should create a data structure for specifying angle and defining its bounds to the max and min duty
        #cycle
        #Note: no change in angles specified here for our particular servos
        MinAngle = 0
        MaxAngle = 180		#maximum angle for a typical servo in degrees

        def AngleToDutyCycle(self, Angle):
            return (Servo.ServoAngle.MaxDutyCycle-Servo.ServoAngle.MinDutyCycle)*(Servo.ServoAngle.MaxAngle-Angle) / (Servo.ServoAngle.MaxAngle-Servo.ServoAngle.MinAngle)

        def DutyCycleToAngle(self, DutyCycle):
            return (self.MaxAngle-self.MinAngle) * (self.MaxDutyCycle - DutyCycle) / (self.MaxDutyCycle - self.MinDutyCycle)

        def DutyCycleLimits():
            input(self.MinDutyCycle, "What is the minimum duty cycle?")
            input(self.MaxDutyCycle, "What is the maximum duty cycle?")

    def SwivelToAngle(self, Angle):
        self.pwm.ChangeDutyCycle(Servo.ServoAngle.AngleToDutyCycle(self, Angle))



def CorrectCameraPosition(Servo, HorizontalError):
    #ErrorToDutyCycle = (MaxDutyCycle-MinDutyCycle)*HorizontalError/2 + (MaxDutyCycle+MinDutyCycle)/2
    Servo.SwivelToAngle(HorizontalError)



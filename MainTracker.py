import ServoControl
import DotFinder
import RulerMeasurement
import timeit

def CenterCameraonRedDot(LaserLocation):
    Camera_width = 80
    #Calculate center from frame data
    #LaserLocation comes back as pair of integer coords within camera frame
    HorizontalError = (LaserLocation.first() - Camera_width/2) / Camera_width #relative error
    ServoControl.CorrectCameraPosition(PWM, HorizontalError)
    
def TestTrackingSpeed():
    ServoControl.Swivel(PWM) #randomize location
    #CameraObject = DotFinder.CameraSetup()
    #start timing here
    RedDot = DotFinder.ReturnRedDotCenter()
    TrackingSpeed = timeit.timeit(CenterCameraonRedDot(RedDot))
    assert(TrackingSpeed < 0.1)

def LaserisinFrame():
    #can attempt to find the laser somewhere within camera range of motion by bisection
    TestAngle = 90
    ServoControl.SwivelToAngle(TestAngle, PWM)
    LaserLocation = DotFinder.ReturnRedDotCenter()
    if (LaserLocation == None):
        ServoControl.SwivelToAngle(TestAngle/2, PWM)
        LaserLocation = DotFinder.ReturnRedDotCenter()
        if (LaserLocation == None):
            TestAngle = TestAngle*3 / 2
            ServoControl.SwivelToAngle(TestAngle, PWM)
    #Can easily turn this into a recursive function to first sweep left, then sweep right
    if (LaserLocation == None):
        return False
    else:
        return True


#some quick self-tests
ServoControl.ServoSetup(17)	#17 is just one possible choice for gpio pin
PWM = ServoControl.ServoStart(17)
ServoControl.Swivel(PWM) #done just to verify that servo code works
#TestTrackingSpeed()	#use this when we want to test the 0.1 second tracking speed requirement

#LaserCamera = DotFinder.CameraSetup()
LaserLocation = DotFinder.ReturnRedDotCenter()
print(LaserLocation)
CenterCameraonRedDot(Camera, LaserLocation)
FinalMeasurement = RulerMeasurement()
FinalMeasurement.ReadMeasurement()
print(FinalMeasurement.measurement + " " + FinalMeasurement.units) 


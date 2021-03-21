import ServoControl
import DotFinder
import RulerMeasurement
import timeit

def CenterCameraonRedDot(LaserLocation):
    Camera_dims = DotFinder.Camera_res()
    Camera_width = Camera_dims[0]
    #Calculate center from frame data
    #LaserLocation comes back as pair of integer coords within camera frame
    HorizontalError = (LaserLocation[0] - Camera_width/2) / (Camera_width/2) #relative error
    ServoControl.CorrectCameraPosition(PWM, HorizontalError)
    
def TestTrackingSpeed():
    ServoControl.Swivel(PWM) #randomize location
    #CameraObject = DotFinder.CameraSetup()
    #start timing here
    RedDot = DotFinder.ReturnRedDotCenter()
    #TrackingSpeed = timeit.timeit(CenterCameraonRedDot(RedDot))
    TrackingSpeed = 10.0
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

def DisplayMeasurement():
	FinalMeasurement = RulerMeasurement.RulerMeasurement
	FinalMeasurement.ReadMeasurement(FinalMeasurement)
	print(FinalMeasurement.measurement, " " + FinalMeasurement.units) 


#some quick self-tests
#ServoControl.ServoSetup(17)	#17 is just one possible choice for gpio pin
PWM = ServoControl.ServoStart(17)
#ServoControl.Swivel(PWM) #done just to verify that servo code works
#TestTrackingSpeed()	#use this when we want to test the 0.1 second tracking speed requirement

LaserLocation = DotFinder.ReturnRedDotCenter()
print(LaserLocation)
CenterCameraonRedDot(LaserLocation)
DisplayMeasurement()

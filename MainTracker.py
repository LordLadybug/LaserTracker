import ServoControl
import DotFinder
import RulerMeasurement
import timeit

def CenterCameraonRedDot(Camera, LaserLocation):
    #Calculate center from frame data
    #LaserLocation comes back as pair of integer coords within camera frame
    HorizontalError = (LaserLocation.first() - Camera.width()/2) / Camera.width() #relative error
    ServoControl.CorrectCameraPosition(PWM, HorizontalError)
    
def TestTrackingSpeed():
    ServoControl.Swivel(PWM) #randomize location
    CameraObject = DotFinder.CameraSetup()
    #start timing here
    RedDot = DotFinder.ReturnRedDotCenter(CameraObject)
    TrackingSpeed = timeit.timeit(CenterCameraonRedDot(CameraObject, RedDot))
    assert(TrackingSpeed < 0.1)


#some quick self-tests
ServoControl.ServoSetup(17)	#17 is just one possible choice for gpio pin
PWM = ServoControl.ServoStart(17)
ServoControl.Swivel(PWM) #done just to verify that servo code works
#TestTrackingSpeed()	#use this when we want to test the 0.1 second tracking speed requirement

LaserCamera = DotFinder.CameraSetup()
LaserLocation = DotFinder.ReturnRedDotCenter(LaserCamera)
print(LaserLocation)
CenterCameraonRedDot(Camera, LaserLocation)
FinalMeasurement = RulerMeasurement()
FinalMeasurement.ReadMeasurement()
print(FinalMeasurement.measurement + " " + FinalMeasurement.units) 


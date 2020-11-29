import ServoControl
import DotFinder
import RulerMeasurement

ServoControl.ServoSetup(17)
PWM = ServoControl.ServoStart(17)
ServoControl.Swivel(PWM) #done just to verify that servo code works

LaserCamera = DotFinder.CameraSetup()
LaserLocation = DotFinder.ReturnRedDotCenter(LaserCamera)
print(LaserLocation)
CenterCameraonRedDot(Camera, LaserLocation)
FinalMeasurement = RulerMeasurement()
FinalMeasurement.ReadMeasurement()
print(FinalMeasurement.measurement + " " + FinalMeasurement.units) 

def CenterCameraonRedDot(Camera, LaserLocation):
    #Calculate center from frame data
    #LaserLocation comes back as pair of integer coords within camera frame
    HorizontalError = LaserLocation.first() - Camera.width()/2
    ServoControl.CorrectCameraPosition(PWM, HorizontalError)
    

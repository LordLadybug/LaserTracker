import MainTracker.py
from tkinter import *

TrackingWindow = Tk()
TrackingWindow.title("Laser Tracking Window")

#measurement number displayed at bottom of window
Measurement = ttk.label(parent, text = "Measurement:  ")
.Measurement configure -textvariable measureNo
set measureNo "Measurement:  " + MainTracker.ReadMeasurement()

#Test Tracking Speed
SpeedTest = ttk.Button(parent, text = "Test tracking speed",
command=MainTracker.TestTrackingSpeed())

#start/stop tracking
ToggleTracking = ttk.Button(parent, text = "Start/stop tracking", command=MainTracker.CenteronRedDot())

#overlay from opencv? maybe can keep as a separate window

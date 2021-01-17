import MainTracker
import RulerMeasurement
from tkinter import *
from tkinter import ttk

def ToggleTrack(*args):
	MainTracker.CenteronRedDot()
	Measure = RulerMeasurement()
	Measure.ReadMeasurement()
	measureNo.set(str(Measure.Measurement) + Measure.units)

TrackingWindow = Tk()
TrackingWindow.title("Laser Tracking Window")
WindowFrame = ttk.Frame(TrackingWindow)
WindowFrame.grid(column=0, row=0, sticky = (N, W, E, S))
TrackingWindow.columnconfigure(0, weight=1)
TrackingWindow.rowconfigure(0, weight=2)
TrackingWindow.columnconfigure(3, weight=2)
TrackingWindow.columnconfigure(6, weight=1)
TrackingWindow.rowconfigure(6, weight=1)

#measurement number displayed at bottom of window
Measurement = ttk.label(parent, text = "Measurement:  ")
.Measurement configure -textvariable measureNo
set measureNo "Measurement:  " + RulerMeasurement.ReadMeasurement()
Measurement.grid(row=4, column=4, sticky=(E, S))

#Test Tracking Speed
SpeedTest = ttk.Button(parent, text = "Test tracking speed",
command=MainTracker.TestTrackingSpeed())
SpeedTest.grid(column=1, row=0, sticky = (W))

#start/stop tracking
ToggleTracking = ttk.Button(parent, text = "Start/stop tracking", command=ToggleTrack)
ToggleTracking.grid(column = 4, row=0, sticky = (E))

for child in TrackingWindow.winfo_children():
	child.grid_configure(padx = 10, pady = 20)
#overlay from opencv? maybe can keep as a separate window

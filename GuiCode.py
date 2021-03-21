import MainTracker
import RulerMeasurement
from tkinter import *
from tkinter import ttk
import DotFinderTesting
import io

def ToggleTrack(*args):
	MainTracker.CenteronRedDot()
	Measure = RulerMeasurement()
	Measure.ReadMeasurement()
	measureNo.set(str(Measure.measurement) + Measure.units)

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
measureNo = StringVar()
Measurement = ttk.Label(TrackingWindow, text = "Measurement:  ")
#measureNo.set("Measurement:  " + str(RulerMeasurement.measurement) + RulerMeasurement.units)
Measurement.grid(row=4, column=4, sticky=(E, S))

#Test Tracking Speed
SpeedTest = ttk.Button(TrackingWindow, text = "Test tracking speed",
command=MainTracker.TestTrackingSpeed())
SpeedTest.grid(column=1, row=0, sticky = (W))

#start/stop tracking
ToggleTracking = ttk.Button(TrackingWindow, text = "Start/stop tracking", command=ToggleTrack)
ToggleTracking.grid(column = 4, row=0, sticky = (E))

for child in TrackingWindow.winfo_children():
	child.grid_configure(padx = 10, pady = 20)
#overlay from opencv? maybe can keep as a separate window

def Exit():
	TrackingWindow.destroy()

def CameraTestRun():
	CameraTestRun = CameraTestSuite()

class CameraTestSuite:
	def __init__(self):
		self.CameraTestWindow = Toplevel(TrackingWindow)
		self.CameraTestWindow.title("Camera test suite")
		self.CamTestFrame = ttk.Frame(self.CameraTestWindow, padding = (2,2,2,2))
		self.CamTestFrame.grid(column=2, row=1, sticky=(N))
		self.Closebutton = ttk.Button(self.CameraTestWindow, text="Close",
		command=self.CloseCameraTest)
		self.Closebutton.grid(column=1, row=2, sticky=(S))
		self.TestResults = Text(self.CameraTestWindow)
		self.TestResults.grid(column=1, row=1, sticky=(N))
		ResultsFetched = self.FetchTestResults()
		self.TestResults.insert('1.0', ResultsFetched.getvalue())
		self.TestResults['state'] = 'disabled'

		def FetchTestResults(self):
			Tests = unittest.defaultTestLoader.loadTestsFromModule(DotFinderTesting)
			ResultsContainer = io.StringIO()
			Results = unittest.TextTestRunner(ResultsContainer)
			Results.run(Tests)
			return ResultsContainer

		def CloseCameraTest(self):
			self.CameraTestWindow.destroy()

#menu
TrackingWindow.option_add('*tearOff', FALSE)
menubar = Menu(TrackingWindow)
TrackingWindow['menu'] = menubar
menu_file = Menu(menubar)
menu_run = Menu(menubar)
menubar.add cascade(menu = menu_file, label='File')
menubar.add cascade(menu = menu_run, label='Run')
menu_file.add_command(label='Exit', command=Exit)
menu_run.add_command(label='Run camera test suite', command=CameraTestSuite)

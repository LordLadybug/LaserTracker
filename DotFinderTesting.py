import DotFinder
import unittest

#test for frame grabbing a non-empty frame
def IsFrameEmpty():
	frame = DotFinder.grabFrame()
	self.assertFalse(frame is empty)

def FrameHasThreeChannels():
	frame = DotFinder.grabFrame()
	self.assertTrue(frame.dim[2] == 3)

def ConvertstoHSV():
	try:
		cv.cvtColor(frame, hsvFrame, cv.color_BGR2HSV)
	except ValueError:
		self.assertRaise(ValueError)

def CorrectLaserPattern():
	RedFrame = DotFinder.IsolateRedDot()
#insert code to calculate shape of the pattern and assert that it is dot-shaped

def CorrectDotSize():
	RedFrame = DotFinder.IsolateRedDot()
	ScreenSize = DotFinder.getResolution()
	DotSize = #code for calculating area of red dot
	assertTrue(DotSize < ScreenSize/4) #dot takes up no more than a quarter of screen

def CorrectForeground():
	self.assertTrue(CorrectLaserPattern())
	self.assertTrue(CorrectDotSize())
#follows from above two test

def LowSensitivitytoDistractors():
	DotCount = #Counts number of dot-like items found
#Compares contours found and can select the most dot-like (round) pattern

def CentroidOnCenter():
	RedFrame = DotFinder.IsolateRedDot()
	retval, cnt = cv.findContours(RedFrame)
	moments = cv.moments(cnt)
	geoCenter = #code to calculate geometric center of dot
	self.assertEqual(geoCenter,int(moments['m10']/moments['m00']),
	int(momentss['m01']/moments['m00']))

#make sure no divisions by zero

#returns x-y coordinates
def Returnsxy():
	Dot = DotFinder.FindRedDot()
#assert that structure of Dot is an integer pair

def CoordsAreInFrame():
	Dot = DotFinder.FindRedDot()
	ScreenSize = DotFinder.getResolution()
	assertTrue(0<= Dot & Dot<=ScreenSize)

def NonEmptyContourList():
	RedFrame = DotFinder.IsolateRedDot()
	retval, cnt = cv.findContours(RedFrame)
	assertFalse(cnt is empty)

def ContoursCenteronDot():
	#define bounds for red dot, then assert contours[0] in inside bounds

def ContoursSensitivetoDistractors():
	#Look for Contours[0] to follow the dot instead of other red objects

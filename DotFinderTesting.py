import DotFinder
import unittest
import cv2 as cv

class DotFinderTest(unittest.TestCase):
	#test for frame grabbing a non-empty frame
	def test_IsFrameEmpty(self):
		frame = DotFinder.grabFrame()
		self.assertFalse(frame is empty)

	def test_FrameHasThreeChannels(self):
		frame = DotFinder.grabFrame()
		self.assertTrue(frame.dim[2] == 3)

	def test_ConvertstoHSV(self):
		try:
			cv.cvtColor(frame, hsvFrame, cv.color_BGR2HSV)
		except ValueError:
			self.assertRaise(ValueError)

	def test_CorrectLaserPattern(self):
		RedFrame = DotFinder.IsolateRedDot()
		contours = (0, 0)
		center, radius = cv.minEnclosingCircle(contours[0])
		self.assertEquals(math.pi()*radius**2, cv.contourArea(contours[0]))
		self.asserTrue(cv.isContourConvex(contours[0]))


	def test_CorrectDotSize(self):
		RedFrame = DotFinder.IsolateRedDot()
		ScreenSize = DotFinder.getResolution()
		DotSize = cv.contourArea(contours[0])
		assertTrue(DotSize < ScreenSize/4) #dot takes up no more than a quarter of screen

	def test_CorrectForeground(self):
		self.assertTrue(CorrectLaserPattern())
		self.assertTrue(CorrectDotSize())
		#follows from above two test

	def test_LowSensitivitytoDistractors(self):
		DotCount = DotFinder.DotCount()
		self.assertEquals(DotCount, 1)
		#Compares contours found and can select the most dot-like (round) pattern

	def test_CentroidOnCenter(self):
		RedFrame = DotFinder.IsolateRedDot()
		retval, cnt = cv.findContours(RedFrame)
		moments = cv.moments(cnt)
		geoCenter, geoRadius = cv.minEnclosingCircle(cnt[0])
		self.assertEqual(geoCenter,int(moments['m10']/moments['m00']),
		int(moments['m01']/moments['m00']))

	def test_NoDivisionByZero(self):
		NoZeroDivision = False
		if (moments['m00'] != 0):
			NoZeroDivision = True
		self.assertTrue(NoZeroDivision)
		#make sure no divisions by zero

	#returns x-y coordinates
	def test_Returnsxy(self):
		Dot = DotFinder.FindRedDot()
		self.assertIsInstance(Dot, (int, int))
		#assert that structure of Dot is an integer pair

	def test_CoordsAreInFrame(self):
		Dot = DotFinder.FindRedDot()
		ScreenSize = DotFinder.getResolution()
		assertTrue(0<= Dot & Dot<=ScreenSize)

	def test_NonEmptyContourList(self):
		RedFrame = DotFinder.IsolateRedDot()
		retval, cnt = cv.findContours(RedFrame)
		assertFalse(cnt is empty)

	def test_ContoursCenteronDot(self):
		self.assertTrue(1)
		#define bounds for red dot, then assert contours[0] in inside bounds

	def test_ContoursSensitivetoDistractors(self):
		self.assertTrue(1)
		#Look for Contours[0] to follow the dot instead of other red objects
		
	#Running the tests:
	if __name__ == '__main__':
		unittest.main()

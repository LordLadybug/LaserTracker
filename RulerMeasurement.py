import numpy as np
import cv2 as cv
import DotFinder
import CameraCVInterface

class RulerMeasurement:
    measurement = 0.0
    units = "cm"

    #returns a measurement by reading the ruler
	#define enum based on whether we're working in inches or cm
    def ReadMeasurement(self):
        measurement = 0.0
        units = RulerMeasurement.FindUnits(RulerMeasurement)
        Markings = RulerMeasurement.CountMarkings(RulerMeasurement)
        for i in range(Markings):
            if (units == "inches"):
                measurement += 1/16
            elif (units == "cm"):
                measurement += 0.1
        return measurement

    def CountMarkings(self):
        NumberofMarkings = 0
        #insert code to find nearest marked number and then count tick marks up to red dot
        NearestMarkedNumber = 0
        CVVideo = CameraCVInterface.CameraCVInterface()
        ruler_frame = CVVideo.GrabFrame()
        #with np.load('knn_data.npz') as data:
        #    print( data.files )
        #    train = data['train']
        #    train_labels = data['train_labels']
        #ret,result,neighbours,dist = knn.findNearest(test,k=5)
        #modify to findNearest on the ruler frames instead and this will give us nearest marked number
        #NearestMarkedNumber = result
        MarkedNumberCoords = 0 #fill in with info on where this number appears in frame
        #now to count tick marks up
        mask = 0 #mask of all black to match printing
		#noise removal
        kernel = np.ones((3,3),np.uint8)
        #opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
        # sure background area
        #sure_bg = cv.dilate(opening,kernel,iterations=3)
        # Finding sure foreground area
        #dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
        #ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
        # Finding unknown region
        #sure_fg = np.uint8(sure_fg)
        #unknown = cv.subtract(sure_bg,sure_fg)
        RedDot = DotFinder.ReturnRedDotCenter()
        #now slowly expand bounding box in positive x direction until our bounding box contains the red dot
		#(x-coordinate >= x-coordinate of red dot)
        return NumberofMarkings

    def FindUnits(self):
	#For now, default to cm
	#later, can use algorithm based on spacing of markings
        units = "cm"
        return units


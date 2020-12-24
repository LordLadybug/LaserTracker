import cv2 as cv
import numpy as np
import CameraCVInterface

#define range of red colors(use HSV scale)
#These are the cutoff values that we will use for the whole program
lower_red = np.array([0,100,31])
upper_red = np.array([14, 100, 100])

def IsolateRedDot():
	CVvideo = CameraCVInterface.CameraCVInterface()
	try:
		frame = CVvideo.GrabFrame()
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	except ValueError:
		CVvideo.EmptyFrameErrorCleanup()
    #Threshold image to filter for red colors
	mask =cv.inRange(hsv, lower_red, upper_red)
	res = cv.bitwise_and(frame, frame, mask= mask)
	cv.imshow('frame',frame)
	cv.imshow('mask',mask)
	cv.imshow('res', res)
	return res

def ReturnRedDotCenter():
    red_frames = IsolateRedDot()
    ret, thresh = cv.threshold(upper_red)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    M = cv.moments(cnt)
    #save as a point to store the center of the red dot
    RedDot = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    return RedDot

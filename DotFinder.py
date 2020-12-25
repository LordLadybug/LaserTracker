import cv2 as cv
import numpy as np
import CameraCVInterface

#define range of red colors(use HSV scale)
#These are the cutoff values that we will use for the whole program
l_r = np.uint8([[[30, 38, 38]]])
u_r = np.uint8([[[180, 84, 67]]])
lower_red = cv.cvtColor(l_r, cv.COLOR_BGR2HSV)	#30 38 38
upper_red = cv.cvtColor(u_r, cv.COLOR_BGR2HSV)  #180 84 67


CVvideo = CameraCVInterface.CameraCVInterface()
def IsolateRedDot():
	try:
		frame = CVvideo.GrabFrame()
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	except ValueError:
		CVvideo.EmptyFrameErrorCleanup()
    #Threshold image to filter for red colors
	mask =cv.inRange(hsv, lower_red, upper_red)
	mask = cv.bitwise_not(mask)
	res = cv.bitwise_and(frame, frame, mask= mask)
	cv.imshow('frame',frame)
	cv.imshow('mask',mask)
	cv.imshow('res', res)
	k = cv.waitKey()
	return mask

def ReturnRedDotCenter():
    isolated_frames = IsolateRedDot()
    ret, thresh = cv.threshold(isolated_frames, 127, 255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    M = cv.moments(cnt)
    #save as a point to store the center of the red dot
    RedDot = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    return RedDot

def Camera_res():
    return CVvideo.get_resolution()

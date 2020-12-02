import cv2 as cv
import picamera
import io
import os
from time import sleep
import numpy as np
import CameraCVInterface

def CameraSetup():
	#Camera.resolution = (320, 240)
	#Camera.framerate = 24
	#image = np.empty((240 * 320 * 3,), dtype=np.uint8)
	#code above may not be necessary?
    Camera = picamera.PiCamera()
    Camera.start_preview()
    #Camera warm-up time
    sleep(2)
#possibly replace with only capturing single images? or wait for an image with red in it, then use
	#that image for processing?
    CameraStream = picamera.PiCameraCircularIO(Camera, seconds = 5)   #replace seconds with OpenCV
    #documented number (can also specify bytes if OpenCV specifies a number of bytes needed)
    Camera.start_recording(CameraStream, 'bgr') #using bgr because OpenCV works with that format
    return CameraStream

def IsolateRedDot(CameraStream):
    #CVCameraObject=cv.VideoCapture(0)
	CVvideo = CameraCVInterface()
	while(CVvideo.is_good()):
	#while(CVCameraObject.isOpened()):
        #frame_exists, frame = CVCameraObject.read()
        #Convert BGR to HSV
	#	if (frame_exists):
	#		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	#	else:
	#		EmptyFrameErrorCleanup()
		frame = CVvideo.GrabFrame()
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        #define range of red colors(use HSV scale)
        lower_red = np.array([0,100,31])
        upper_red = np.array([14, 100, 100])

        #Threshold image to filter for red colors
        mask =cv.inRange(hsv, lower_red, upper_red)
        res = cv.bitwise_and(frame, frame, mask= mask)
        cv.imshow('frame',frame)
        cv.imshow('mask',mask)
        cv.imshow('res', res)
        k = cv.waitKey(5) & 0xFF
        #if k==27:
	#    cv.destroyAllWindows()
	#    Camera.stop_recording()
	#    Camera.stop_preview()
	#    break
    
#bunch of cleanup code, may need to be put elsewhere
    cv.destroyAllWindows()
	cv.ReleaseCapture()
    Camera.stop_recording()
    Camera.stop_preview()
	CameraStream.clear()
    return Camera

def ReturnRedDotCenter(Camera):
    IsolateRedDot(Camera)
    ret, thresh = cv.threshold(upper_red)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    M = cv.moments(cnt)
    #save as a point to store the center of the red dot
    RedDot = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    return RedDot

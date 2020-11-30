import cv2 as cv
import picamera
import io
import os
from time import sleep
import numpy as np

def CameraSetup():
    Camera = picamera.PiCamera()
    Camera.add_overlay()
    #Camera warm-up time
    sleep(2)
    CameraStream = Camera.PiCameraCircularIO(Camera, seconds = 5)   #replace seconds with OpenCV
    #documented number (can also specify bytes if OpenCV specifies a number of bytes needed)
    Camera.start_recording(CameraStream, 'bgr') #using bgr because OpenCV works with that format
    return CameraStream

def IsolateRedDot(CameraStream):
    CVCameraObject=cv.VideoCapture(CameraStream)
    while(CVCameraObject.isOpened()):
        _, frame = CVCameraObject.read()
        #Convert BGR to HSV
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
    
    cv.destroyAllWindows()
    Camera.stop_recording()
    Camera.stop_preview()
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

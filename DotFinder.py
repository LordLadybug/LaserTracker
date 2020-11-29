import cv2 as cv
import picamera
import io
import os
from time import sleep
import numpy as np
import multiprocessing

def CameraSetup():
    os.mkfifo('video_fifo')
    Camera = picamera.PiCamera()
    Camera.start_preview()
    #Camera warm-up time
    sleep(2)
    CameraStreamIn, CameraStreamOut = MakeVideoPipe(Camera) #change to whatever stream object I end up
    #using
    return CameraStreamOut

def SendVideo(CameraStreamIn, Camera):
    Camera.start_recording(CameraStreamIn, 'bgr')   #bgr is the preferred format for OpenCV
    CameraStreamIn.send()
    CameraStreamIn.close()

def ReceiveVideo(CameraStreamOut):
    CameraStreamOut.recv()
    CameraStreamOut.close()

def IsolateRedDot(CameraStream):
    CVCameraObject=cv.VideoCapture(CameraStream)
    while(1):
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
        if k==27:
	    cv.destroyAllWindows()
	    Camera.stop_recording()
	    Camera.stop_preview()
	    os.unlink('video_fifo')
            break
    
    cv.destroyAllWindows()
    Camera.stop_recording()
    Camera.stop_preview()
    os.unlink('video_fifo')
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

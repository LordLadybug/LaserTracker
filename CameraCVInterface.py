import picamera
import cv2 as cv

#may need to move camera setup code from DotFinder into here (probably)

class CameraCVInterface():	#is a class definition necessary here?

	def CameraSetup():
		#Camera.resolution = (320, 240)
		#Camera.framerate = 24
		#image = np.empty((240 * 320 * 3,), dtype=np.uint8)
		#code above may not be necessary?
		Camera = picamera.PiCamera()
		Camera.start_preview()
		#Camera warm-up time
		sleep(2)
		#possibly replace with only capturing single images? or wait for an image with red
		#in it, then use that image for processing?
		CameraStream = picamera.PiCameraCircularIO(Camera, seconds = 5)   #replace seconds with OpenCV
		#documented number (can also specify bytes if OpenCV specifies a number of bytes needed)
		Camera.start_recording(CameraStream, 'bgr') #using bgr because OpenCV works with that format
		return CameraStream

	def GrabFrame(CameraStream):
		PiCameraStream = CameraSetup()
		OpenCVObject = cv.VideoCapture(PiCameraStream)
		FrameExists, Frame = OpenCVObject.read()
		if (FrameExists):
			return Frame
		else:
			EmptyFrameErrorCleanup()
	
	 def EmptyFrameErrorCleanup():
		raise ValueError("OpenCV attempted to read an empty frame")
		Camera.stop_recording()
		Camera.stop_preview()
		break

	def is_good():
		return CameraStream.is_opened()	&& FrameExists
		

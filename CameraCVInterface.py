import picamera
import numpy as np

#may need to move camera setup code from DotFinder into here (probably)

class CameraCVInterface():
	def CameraSetup():
		Camera.resolution = (320, 240)
		Camera.framerate = 24
		image = np.empty((240 * 320 * 3,), dtype=np.uint8)
		Camera = picamera.PiCamera()
		Camera.start_preview()
		#Camera warm-up time
		sleep(2)
		return Camera

	def GrabFrame():
		Camera = CameraSetup()
		CameraStream = Camera.capture(image, 'bgr')
		FrameExists = image.all() == None
		if (FrameExists):
			return Frame
		else:
			EmptyFrameErrorCleanup()

	def EmptyFrameErrorCleanup():
		raise ValueError("OpenCV attempted to read an empty frame")


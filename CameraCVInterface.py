import picamera
import numpy as np
from time import sleep

#may need to move camera setup code from DotFinder into here (probably)

class CameraCVInterface():
	Camera = picamera.PiCamera()

	def CameraSetup(self):
		self.Camera.resolution = (320, 240)
		self.Camera.framerate = 24
		self.Camera.start_preview()
		#Camera warm-up time
		sleep(2)

	def GrabFrame(self):
		self.CameraSetup()
		image = np.empty((240 * 320 * 3,), dtype=np.uint8)
		self.Camera.capture(image, 'bgr')
		FrameExists = (image.all() == None)
		return image

	def EmptyFrameErrorCleanup(self):
		raise ValueError("OpenCV attempted to read an empty frame")
		self.Camera.stop_preview()


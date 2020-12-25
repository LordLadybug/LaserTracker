import picamera
import numpy as np
from time import sleep

class CameraCVInterface():
	Camera = picamera.PiCamera()

	def CameraSetup(self):
		self.Camera.resolution = (320, 240)
		self.Camera.framerate = 24
		#Camera warm-up time
		sleep(2)

	def GrabFrame(self):
		self.CameraSetup()
		image_np = np.empty((320 * 240 * 3,), dtype=np.uint8)	
		self.Camera.capture(image_np, 'bgr')
		image = image_np.reshape((240,320,3))
		return image

	def EmptyFrameErrorCleanup(self):
		raise ValueError("OpenCV attempted to read an empty frame")

	def get_resolution(self):
		return self.Camera.resolution

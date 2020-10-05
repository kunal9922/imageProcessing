import cv2 as cv
import numpy as np

class UtilsCode:
	''' HSV hue saturation value
			HUE = color
			saturation = how pure color is
			value= how bright color is '''
	def __init__(self, frameHeight=360, frameWidth=360):
		self.frameHeight = frameHeight
		self.frameWidth =frameWidth
		cv.namedWindow("HSV color space")
		cv.resizeWindow("HSV color space", self.frameWidth, self.frameHeight)
		# in HSV Hue is range from 0 - 360 but in open cv 0-179
		cv.createTrackbar("hue min", "HSV color space", 0, 179, lambda: True)
		cv.createTrackbar("hue max", "HSV color space", 179, 179, lambda: True)
		cv.createTrackbar("sat min", "HSV color space", 0, 255, lambda: True)
		cv.createTrackbar("sat max", "HSV color space", 255, 255, lambda: True)
		cv.createTrackbar("val min", "HSV color space", 0, 255, lambda: True)
		cv.createTrackbar("val max", "HSV color space", 255, 255, lambda: True)

	def utilfunc(self,img):
		# converting BLUE GREEN RED image to HUE SATURATION VALUE
		img = cv.resize(img, (360, 360))
		imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		# get values from track bar

		''' keep preserve which color you want  and move track bar according to it'''
		hmin = cv.getTrackbarPos("hue min", "HSV color space")
		hmax = cv.getTrackbarPos("hue max", "HSV color space")
		smin = cv.getTrackbarPos("sat min", "HSV color space")
		smax = cv.getTrackbarPos("sat max", "HSV color space")
		vmin = cv.getTrackbarPos("val min", "HSV color space")
		vmax = cv.getTrackbarPos("val max", "HSV color space")

		lower = np.array([hmin, smin, vmin])
		upper = np.array([hmax, smax, vmax])
		# inRange returns the range between the variables  are provided
		mask = cv.inRange(imgHSV, lower, upper)

		result = cv.bitwise_and(img, img, mask=mask)
		# merge original image and resultant image together
		# so that it's easier to track the output which we want

		# covert mask image have one channel so that we can't merge with 3channel image. so do convert it
		mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
		hstack = np.hstack([img, result, mask])

		cv.imshow("Result", hstack)


	def detectvid(self, cap):
		# capturing frames from video and find out the color using HSV
		self.cap = cap

		while self.cap.isOpened():
			res, img = self.cap.read()
			self.utilfunc(img)

			if cv.waitKey(1) & 0xFF == ord("q"):  # for quit the session
				break

		# release memory video capture obj.
		cap.release()

	def detectImg(self, img):
		'''takes a image to be detect'''
		self.img = img

		while True:
			image = cv.imread(img)
			self.utilfunc(image)

			if cv.waitKey(1) & 0xFF == ord("q"):
				break



class DetectColor:
	def __init__(self, **input):
		self.input = input
		if "frameHeight" in input.keys() and "frameWidth" in input.keys():
			self.frameHeight = input["frameHeight"]
			self.frameWidth = input["frameWidth"]
		else:
			self.frameHeight = 0
			self.frameWidth = 0

		'''0: means for first camera ,1 means second camera , path:str for specific data'''
		if "image" in input["image"].keys():
			# from image
			try:
				call = UtilsCode(frameHeight=self.frameHeight, frameWidth=self.frameWidth)
				img = self.readImg(self.input["image"])
				call.detectImg(img)

			except KeyError:
				call = UtilsCode()
				img = self.readImg(self.input["image"])
				call.detectImg(img)
		# for video capturing
		elif "video" in input["video"].keys():
			try:
				call = UtilsCode(frameHeight=input["frameHeight"], frameWidth=input["frameWidth"])
				cap = self.readVid(input["video"])
				call.detectvid(cap)

			except KeyError:
				call = UtilsCode()
				cap = self.readVid(input["video"])
				call.detectvid(cap)

	def readVid(self, inp): # for capturing video object creation
		cap = cv.VideoCapture(inp)
		cap.set(3, 360)
		cap.set(4, 360)
		return cap

	def readImg(self, inp): # reading image from given input
		img = cv.imread(inp)
		if self.frameHeight and self.frameWidth:
			resizeImg = cv.resize(img, (self.frameHeight, self.frameWidth))
			return resizeImg
		else:
			return img






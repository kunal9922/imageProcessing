import cv2 as cv
import numpy as np

# create object for capturing the video
cap = cv.VideoCapture(r"C:\Users\kunal\PycharmProject\Opencv\img_vid\project_video.mp4")
# frame Sizes are
frameWidth = 360
frameHeight = 360
cap.set(3, frameWidth)
cap.set(4, frameWidth)


def nothing():
	pass  # call back function if trackbar moves


''' HSV hue saturation value
		HUE = color 
		saturation = how pure color is 
		value= how bright color is '''

cv.namedWindow("HSV color space")
cv.resizeWindow("HSV color space",  frameWidth, frameHeight)
	# in HSV Hue is range from 0 - 360 but in open cv 0-179
cv.createTrackbar("hue min", "HSV color space", 0, 179, nothing)
cv.createTrackbar("hue max", "HSV color space", 179, 179, nothing)
cv.createTrackbar("sat min", "HSV color space", 0, 255, nothing)
cv.createTrackbar("sat max", "HSV color space", 255, 255, nothing)
cv.createTrackbar("val min", "HSV color space", 0, 255, nothing)
cv.createTrackbar("val max", "HSV color space", 255, 255, nothing)

# capturing frames from video and find out the color
while cap.isOpened():
	res, img = cap.read()

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
	if cv.waitKey(1) & 0xFF == ord("q"):
		break
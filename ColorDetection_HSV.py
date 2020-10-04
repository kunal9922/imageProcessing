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

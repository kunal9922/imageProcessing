import cv2 as cv
import numpy as np

# create object for capturing the video
cap = cv.VideoCapture(r"C:\Users\kunal\PycharmProject\Opencv\img_vid\project_video.mp4")
# frame Sizes are
frameWidth= 360
frameHeight =360
cap.set(3, frameWidth)
cap.set(4, frameWidth)


import cv2 as cv
import os

class stichImage:
	def __init__(self, folderPath: str):
		mainFolder = "imagesDataSet"
		#   fetching all the folder names
		myFolders = os.listdir(mainFolder)  # return total no. of folders are  in main folder
		print(myFolders)

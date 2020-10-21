import cv2 as cv
import os

class stichImage:
	def __init__(self, folderPath: str):
		self.mainFolder = folderPath
		#   fetching all the folder names
		myFolders = os.listdir(self.mainFolder)  # return total no. of folders are  in main folder
		print(myFolders)

		# if other more folder are in main directory so fetch that
		for folder in myFolders:
			path = self.mainFolder + '//'+folder
			self.images = []  # empty list for storing images
			myList = os.listdir(path) # return all images for specific path
			print(myList)


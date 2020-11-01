import cv2 as cv
import os

class stichImage:
	def __init__(self, folderPath: str):
		self.mainFolder = folderPath
		#   fetching all the folder names
		myFolders = os.listdir(self.mainFolder)  # return total no. of folders are  in main folder
		print("Folder Names are : ",myFolders)

		# if other more folder are in main directory so fetch that
		for folder in myFolders:
			path = self.mainFolder + '//'+folder
			self.images = []  # empty list for storing images
			myList = os.listdir(path) # return all images for specific path

			print(f"Total images are detected {len(myList)}")
			# iterate to all images are inside the folder
			for imgN in myList:
					currImg = cv.imread(f'{path}//{imgN}')
					currImg = cv.resize(currImg, (0,0), None, 0.2, 0.2) # resizing for show in window screen properly.
					self.images.append(currImg)
					print(self.images)

			# opencv class for stitch images and make a paronama image
			stitcher = cv.Stitcher.create()
			(status, result) = stitcher.stitch(self.images) #  return two status = able to stitch image and result is paronama images
                        cv.imshow("Result image ", result)
			print(status, "", cv.STITCHER_OK )

			if(status == cv.STITCHER_OK):
				print("Paronama Generated")
				cv.imshow(folder, result)
				cv.waitKey(1)
			else:
				print("Paronama Generation Unsuccessfull  ")

		cv.waitKey(0)


if __name__ == '__main__':
	paronama = stichImage("ImagesDataSet")

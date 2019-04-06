import numpy as np
import cv2
import copy

def demosaick( image, filt ):
	newImage = np.zeros((image.shape[0], image.shape[1], 3))
	size = len(filt)
	sizeEach = len(filt[0])

	for i in range(image.shape[0]-size+1):
		for j in range(image.shape[1]-size+1):
			#Figure out what the structure of the filter is like at this position
			blues = np.where(filt == 0)
			greens = np.where(filt == 1)
			reds = np.where(filt == 2)

			#Now with the locations, get the BGR averages
			for x,y in zip(blues[0], blues[1]):
				newImage[i][j][0] += image[i+x][j+y]
			newImage[i][j][0] = newImage[i][j][0]/len(blues[0])

			for x,y in zip(greens[0], greens[1]):
				newImage[i][j][1] += image[i+x][j+y]
			newImage[i][j][1] = newImage[i][j][1]/len(greens[0])

			for x,y in zip(reds[0], reds[1]):
				newImage[i][j][2] += image[i+x][j+y]
			newImage[i][j][2] = newImage[i][j][2]/len(reds[0])

			#Change the structure to match the next column
			filt = np.roll(filt, 1, axis  = 1)

		#Change the structure to match the next row
		filt = np.roll(filt, 1, axis  = 1)
		filt = np.roll(filt, 1, axis = 0)
	
	return np.uint8(newImage)

def colour_filter( image, filt ):
	newImage = np.zeros((image.shape[0], image.shape[1]))
	size = len(filt)

	for i in range(image.shape[0]-size+1):
		for j in range(image.shape[1]-size+1):
			newImage[i][j] = image[i][j][filt[0][0]]
			#Change the structure to match the next column
			filt = np.roll(filt, 1, axis  = 1)
		#Change the structure to match the next row
		filt = np.roll(filt, 1, axis  = 1)
		filt = np.roll(filt, 1, axis = 0)

	return np.uint8(newImage)


if __name__ == '__main__':
	filename = "waterplane.ppm"
	image = cv2.imread(filename)
	#Square filters please
	filt = [[0,1],[1,2]]
	filt = np.array(filt)

	print("Processing", filename)
	RawImage = colour_filter( image, filt )
	print("Done making filter array version")
	DemImage = demosaick( RawImage, filt )
	print("Done demosaicking!")

	A = np.hstack((image, cv2.cvtColor(RawImage, cv2.COLOR_GRAY2BGR), DemImage))
	cv2.imwrite("AllThree"+filename[:-4]+".png", A)
	
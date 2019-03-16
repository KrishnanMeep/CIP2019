import numpy as np
import cv2
import copy

def Euclidean(x,y):
	return np.sqrt(np.sum((x-y)**2))

###########################################################################################
#The Median Filters

#Vecotr Version
def VectorMedianFilter(image):
	newImage = copy.deepcopy(image)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			neighbours = image[i-1:i+2, j-1:j+2].reshape(9,3)
			mu = np.mean(neighbours, axis = 0)
			distances = [ Euclidean(x, mu) for x in neighbours ]
			newImage[i,j] = neighbours[np.argmin(distances)]
	return newImage

#Uses a window, applied for all three channels separately
def MedianFilter( image, size ):
	newImage = copy.deepcopy(image)
	n = size//2
	for i in range(n, image.shape[0]-n):
		for j in range(n, image.shape[1]-n):
			neighbours = image[i-n:i+n+1, j-n:j+n+1].reshape(9,3)
			medians = []
			for k in range(3):
				medians.append(np.median(neighbours[:, k]))
			newImage[i,j] = np.array(medians)
	return newImage

###########################################################################################

#General Convolution Function
def Convolver( image, mask ):
	n = len(mask[0])//2
	newImage = copy.deepcopy(image)

	for i in range(n, image.shape[0]-n):
		for j in range(n, image.shape[1]-n):
			for k in range(3):
				neighbours = image[i-n:i+n+1, j-n:j+n+1, k]
				SOP = 0
				for rowMask,rowNeigh in zip(mask,neighbours):
					for eleMask, eleNeigh in zip(rowMask, rowNeigh):
						SOP += eleMask*eleNeigh
				newImage[i,j,k] = np.clip(SOP, 0, 255)
	return newImage

#The vector versions of prewitts
def PrewittsVFilter(image):
	newImage = copy.deepcopy(image)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			leftSide = image[i-1:i+2, j-1].reshape(3,3)
			rightSide = image[i-1:i+2, j+1].reshape(3,3)
			rightMu = np.mean(rightSide, axis = 0)
			leftMu = np.mean(leftSide, axis = 0)
			newImage[i,j] = abs(rightMu-leftMu)
	return newImage

def PrewittsHFilter(image):
	newImage = copy.deepcopy(image)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			topSide = image[i-1, j-1:j+2].reshape(3,3)
			bottomSide = image[i+1, j-1:j+2].reshape(3,3)
			topMu = np.mean(topSide, axis = 0)
			bottomMu = np.mean(bottomSide, axis = 0)
			newImage[i,j] = abs(topMu-bottomMu)
	return newImage



##########################################################################################


if __name__ == '__main__':
	#The median filters
	image = cv2.imread("balloons_noisy.PNG")

	newImage = VectorMedianFilter(image)
	cv2.imwrite("VectorMedianFilter.PNG", newImage)
	print("Done with Vector Median")
	
	newImage2 = MedianFilter(image, 3)
	cv2.imwrite("ScalarMedianFilter.PNG", newImage2)
	print("Done with Scalar Median")

	#The edge detectors
	image = cv2.imread("me.JPG")
	image = cv2.resize( image, (image.shape[1]//2, image.shape[0]//2))

	newImage3 = Convolver( image, np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))	#Prewitts Vertical with Convolution
	cv2.imwrite("VerticalEdge.PNG", newImage3)
	print("Done with Prewitts Vertical Edge Detector with Convolution")

	newImage4 = PrewittsVFilter( image )
	cv2.imwrite("VectorVertical.PNG", newImage4)
	print("Done with the vector version of Prewitts Vertical Edge Detector")

	newImage5 = Convolver( image, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))	#Prewitts Horizontal with Convolution
	cv2.imwrite("HorizontalEdge.PNG", newImage5)
	print("Done with Prewitts Horizontal Edge Detector with Convolution")

	newImage6 = PrewittsHFilter( image )
	cv2.imwrite("VectorHorizontal.PNG", newImage6)
	print("Done with the vector version of Prewitts Horizontal Edge Detector")

	
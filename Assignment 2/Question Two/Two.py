import numpy as np
import cv2
import copy

def MyDiffusion( image ):
	diffMatrix = np.uint32(copy.deepcopy(image))
	print(diffMatrix.shape)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			error = 0
			if diffMatrix[i][j] < 128:
				error = diffMatrix[i][j]
				diffMatrix[i][j] = 0
			else:
				error = diffMatrix[i][j]-255
				diffMatrix[i][j] = 255

			diffMatrix[i][j+1] = np.clip(18/340*error+diffMatrix[i][j+1], 0, 255)
			diffMatrix[i+1][j] = np.clip(62/340*error+diffMatrix[i+1][j], 0, 255)
			diffMatrix[i+1][j+1] = np.clip(260/340*error+diffMatrix[i+1][j+1], 0, 255)

	diffMatrix = np.uint8(diffMatrix)
	cv2.imwrite("MyDiff.png", diffMatrix)

def MyDiffusion2( image ):
	diffMatrix = np.uint32(copy.deepcopy(image))
	print(diffMatrix.shape)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-2):
			error = 0
			if diffMatrix[i][j] < 128:
				error = diffMatrix[i][j]
				diffMatrix[i][j] = 0
			else:
				error = diffMatrix[i][j]-255
				diffMatrix[i][j] = 255

			diffMatrix[i+1][j+1] = np.clip(80/219*error+diffMatrix[i+1][j+1], 0, 255)
			diffMatrix[i+1][j-1] = np.clip(94/219*error+diffMatrix[i+1][j-1], 0, 255)
			diffMatrix[i+1][j+2] = np.clip(45/219*error+diffMatrix[i+1][j+2], 0, 255)

	diffMatrix = np.uint8(diffMatrix)
	cv2.imwrite("MyDiff2.png", diffMatrix)

def FloydSteinDiffusion( image ):
	diffMatrix = np.uint32(copy.deepcopy(image))
	print(diffMatrix.shape)
	for i in range(1, image.shape[0]-1):
		for j in range(1, image.shape[1]-1):
			error = 0
			if diffMatrix[i][j] < 128:
				error = diffMatrix[i][j]
				diffMatrix[i][j] = 0
			else:
				error = diffMatrix[i][j]-255
				diffMatrix[i][j] = 255

			diffMatrix[i][j+1] = np.clip(7/16*error+diffMatrix[i][j+1], 0, 255)
			diffMatrix[i+1][j] = np.clip(5/16*error+diffMatrix[i+1][j], 0, 255)
			diffMatrix[i+1][j-1] = np.clip(3/16*error+diffMatrix[i+1][j-1], 0, 255)
			diffMatrix[i+1][j+1] = np.clip(1/16*error+diffMatrix[i+1][j+1], 0, 255)

	diffMatrix = np.uint8(diffMatrix)
	cv2.imwrite("FSDiff.png", diffMatrix)

if __name__ == '__main__':
	image = cv2.imread("ed-eg.png", 0)
	FloydSteinDiffusion(image)
	MyDiffusion(image)
	MyDiffusion2(image)
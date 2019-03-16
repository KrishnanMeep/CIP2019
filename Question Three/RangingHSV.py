import numpy as np
import cv2
import copy


def ColourRangingHSV( image, h_c, h_bw, s_c, v_c ):
	#The range for hue
	rangeH = [h_c + h_bw, h_c - h_bw]
	rangeH[0], rangeH[1] = np.clip(rangeH[0], 0, 180), np.clip(rangeH[1], 0, 180)
	
	print(rangeH)

	#The ranging operation
	newImage = copy.deepcopy(image)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			if image[i,j,0] < rangeH[1] or image[i,j,0] > rangeH[0]:
				newImage[i,j,0] = 0
			if image[i,j,1] < s_c:
				newImage[i,j,1] = 0
			if image[i,j,2] < v_c:
				newImage[i,j,2] = 0
	return newImage


if __name__ == '__main__':
	image = cv2.imread("figurines.JPG")
	hsvImage = cv2.cvtColor( image, cv2.COLOR_BGR2HSV)

	print("Ranging Charizard and Lucario...")

	charizard = ColourRangingHSV( hsvImage, 15, 3, 160, 180 )
	charizard = cv2.cvtColor( charizard, cv2.COLOR_HSV2BGR)
	cv2.imwrite("Charizard.PNG", charizard)

	lucario = ColourRangingHSV( hsvImage, 100, 5, 150, 170 )
	lucario = cv2.cvtColor( lucario, cv2.COLOR_HSV2BGR )
	cv2.imwrite("Lucario.PNG", lucario)

	print("Done")
	
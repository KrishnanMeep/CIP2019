import numpy as np
import cv2
import copy


def ColourRangingRGB( image, r_c, r_bw, g_c, g_bw, b_c, b_bw ):
	#The ranges for the three colors according to the center and bandwith, (upper, lower)
	rangeR, rangeG, rangeB = [r_c + r_bw, r_c - r_bw], [g_c + g_bw, g_c - g_bw], [b_c + b_bw, b_c - b_bw]

	#Making sure nothing goes out of bound
	rangeR[0], rangeR[1]= np.clip(rangeR[0], 0, 255), np.clip(rangeR[1], 0, 255)
	rangeG[0], rangeG[1]= np.clip(rangeG[0], 0, 255), np.clip(rangeG[1], 0, 255)
	rangeB[0], rangeB[1]= np.clip(rangeB[0], 0, 255), np.clip(rangeB[1], 0, 255)

	#The ranging operation
	newImage = copy.deepcopy(image)

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			#Check if it lies outside the range
			if image[i,j,2] < rangeR[1] or image[i,j,2] > rangeR[0]:
				newImage[i,j,2] = 0
			if image[i,j,1] < rangeG[1] or image[i,j,1] > rangeG[0]:
				newImage[i,j,1] = 0
			if image[i,j,0] < rangeB[1] or image[i,j,0] > rangeB[0]:
				newImage[i,j,0] = 0
	return newImage


if __name__ == '__main__':
	image = cv2.imread("Viridian.PNG")

	print("Ranging out the flame and the logo...")
	flames = ColourRangingRGB( image, 200, 20, 200, 20, 0, 0 )
	logo = ColourRangingRGB( image, 225, 15, 225, 15, 225, 20)
	cv2.imwrite("TheFlame.PNG", flames)
	cv2.imwrite("TheLogo.PNG", logo)
	print("Done")

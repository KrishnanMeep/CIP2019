import numpy as np
import cv2

#RGB Ordered dot dithering based on this ordered mask I made
# M = [ G1 B1 G7 G5 
#		R1 G6 G2 R3
#		B2 G4 R2 B3
#		G3 B4 R4 B5]
def RGBColorDither( image ):
	dithered = np.zeros((image.shape[0]*4, image.shape[1]*4, 3), np.uint8)
	redplaces = [[1,0],[2,2],[1,3],[3,2]]
	blueplaces = [[0,1],[2,0],[2,3],[3,1],[3,3]]
	greenplaces = [[0,0],[1,2],[3,0],[2,1],[0,3],[1,1],[0,2]]

	#Calculating thresholds for R,G and B
	reddivider = 256//len(redplaces)
	bluedivider = 256//len(blueplaces)
	greendivider = 256 //len(greenplaces)

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			#How much 4x4 space do we need to fill with the colors for this pixel
			redDots = image[i,j,2]//reddivider
			greenDots = image[i,j,1]//greendivider
			blueDots = image[i,j,0]//bluedivider

			#Where are we in the enlarged image with respect to the original image
			x, y = i*4, j*4
			#Put dots in the order specified upto the threshold
			for k in range(redDots):
				dithered[x+redplaces[k][0],y+redplaces[k][1]] = [0,0,255]
			for k in range(greenDots):
				dithered[x+greenplaces[k][0],y+greenplaces[k][1]] = [0,255,0]
			for k in range(blueDots):
				dithered[x+blueplaces[k][0],y+blueplaces[k][1]] = [255,0,0]

	return dithered

#CMY Ordered dot dithering based on this ordered mask I made
# M = [ Y1 C1 M4 C4 
#		Y3 M1 C5 M2
#		C6 M3 M5 C2
#		Y5 C3 Y2 Y4]
def CMYColorDither( image ):
	dithered = np.full((image.shape[0]*4, image.shape[1]*4, 3), 255, dtype = np.uint8)
	cyanPlaces = [[0,1],[2,3],[3,1],[0,3],[1,2],[2,0]]
	yellowPlaces = [[0,0],[3,2],[1,0],[3,3],[3,0]]
	magentaPlaces = [[1,1],[1,3],[2,1],[0,2],[2,2]]

	#Calculating thresholds for R,G and B
	cyanDivider = 256//len(cyanPlaces)
	yellowDivider = 256//len(yellowPlaces)
	magentaDivider = 256 //len(magentaPlaces)

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			#How much 4x4 space do we need to fill with the colors for this pixel
			cyanDots = (255 - image[i,j,2])//cyanDivider
			yellowDots = (255 - image[i,j,0])//yellowDivider
			magentaDots = (255 - image[i,j,1])//magentaDivider

			#Where are we in the enlarged image with respect to the original image
			x, y = i*4, j*4
			#Put dots in the order specified upto the threshold
			for k in range(cyanDots):
				dithered[x+cyanPlaces[k][0],y+cyanPlaces[k][1]] = [255,255,0]
			for k in range(yellowDots):
				dithered[x+yellowPlaces[k][0],y+yellowPlaces[k][1]] = [0,255,255]
			for k in range(magentaDots):
				dithered[x+magentaPlaces[k][0],y+magentaPlaces[k][1]] = [255,0,255]

	return dithered

if __name__ == '__main__':
	filename = "waterplane.ppm"
	print("Processing", filename)
	image = cv2.imread(filename)
	RGB = RGBColorDither(image)
	CMY = CMYColorDither(image)
	print("Done")

	cv2.imwrite(filename[:-4]+"Dithered"+".png", np.hstack((cv2.resize(image, (0,0), fx = 4, fy = 4), RGB, CMY)))

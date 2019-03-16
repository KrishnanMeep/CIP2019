CIP Assignment 1 - Sem 2
-----------------------------------------------------------------------------------------------

ASSIGNMENT 1
Due Date: 22 March 2019
Each question carries 5 Marks.

1.Search the Web for Cumani colour edge detector and write a report on it. Analyse 
how it may be better than doing Sobel edge detection three times on an RGB image.

2.Implement colour ranging operation in RGB space on colour images. The inputs for your 
operation are a colour image and a colour range specification as r_c, r_bw, g_c, g_bw, b_c,
 b_bw where r_c stands for red colour value, r_bw is the width of the range, i.e., colours 
between r_c - r_bw and r_c + r_bw must be retained in the image and all other 'r' values 
should be set to 0. The other parameters are for green and blue colours. You should handle 
errors when values go out of range.

3.Implement colour ranging operation in HSV space on colour images. The inputs for your 
operation are a colour image and a colour range specification as h_c, h_bw, s_c, v_c where
 h_c stands for hue value, h_bw is the width of the range, i.e., colours between h_c - h_bw
 and h_c + h_bw must be retained in the image and all other hue values should be set to 0. 
The parameter s_c is a saturation threshold. Only those pixels with saturation value above
 the threshold should be retained. The parameter v_c is a value threshold and only pixels 
with value greater than v_c should be retained. You should handle errors when values go out 
of range.

4.Implement vector median filter and any one of the basic vector edge detectors. Show example
 images to demonstrate that these are better than the grayscale versions for colour images.


--------------------------------------------------------------------------------------------------

The report for the above is in the pdf file called 18MCMI09_CIPAssignment1
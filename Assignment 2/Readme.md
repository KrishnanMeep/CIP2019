ASSIGNMENT - II

Due Date: 12 April 2019

Simulating Printers & Cameras
---------------------------------------------------------------------------------------------------------------
1. Search the web for Colour Halftoning algorithms. Select one of them and write a detailed report on it
OR implement the selected algorithm and show results on the test images.

2. Try coming up with your own error diffusion coefficients and implement the standard error-diffusion 
algorithm. Compare the performance of your coefficients against Floyd-Steinberg's on this image. Discuss
the patterns visible in yours and in Floyd-Steinberg's at the various gray levels.

3. Implement an algorithm to simulate the grayscale output from a colour filter array. The function prototype is
      image colour_filter (image, filter)
 That is, it takes an input colour image and a colour filter as parameters and returns a grayscale image.
 Implement a demosaicking algorithm with the prototype
      image demosaic (image, filter)
The input image is a grayscale image output by the colour_filter algorithm and the corresponding filter array; 
the output is a colour image.

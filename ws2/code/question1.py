
"""
Group Number: ..........
Group Names :
     Last name , First name
     .......
     .......


"""

"""
Question 1: Getting familiar with image manipulation in python - opencv
Read the image "bicycle.bmp" from the <data> directory
using opencv flag cv2.IMREAD_UNCHANGED
and then find and print the following information about this image

a)	find image height (number of rows)
b)	find image width (number of columns)
c)	find image number of channels
d)	find image datatype
e)	find image number of pixels
f)	convert the image to gray level and then save it in output directory as "bicyclegray.jpg"
g)	find the maximum value of the pixel values
h)	Calculate the mean/average of the pixel values
i)	Change the pixel values of the image in the following way:
    all pixels’ values less than the average value calculated at (h) will be equal to 0
    and all the other pixels will be equal to 1. Then, save it in output directory as "bicycleoutA.jpg"
j)	What type of image that is  generated at (i)?




no need to do this
Repeat the about information using the following opencv flag
cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE

"""


import cv2

import numpy as np

if __name__ == '__main__':

    ############################
    ### TODO: YOUR CODE HERE ###



    # raise NotImplementedError('Implementation for `Question ` in `workshop2` is missing')

    #f)	convert the image to gray level and then save it in output directory as "bicyclegray.jpg"

    bicycleImg = cv2.imread("./../data/bicycle.bmp")

    cv2.imshow('Original image', bicycleImg)

    bicyclegray = cv2.cvtColor(bicycleImg, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Question 1 F: Bicycle in GreyScale', bicyclegray)

    cv2.imwrite("./../output/bicyclegray.jpg", bicyclegray)

    # g)	find the maximum value of the pixel values
    # Assuming max value of the bicyclegray image

    bicyclegreyMax = np.amax(bicyclegray)

    print("Maximum value of the pixels are", bicyclegreyMax)

    # h)	Calculate the mean/average of the pixel values

    bicyclegrayAvg = np.mean(bicyclegray)

    print("Mean/ average of the pixel values are ", bicyclegrayAvg)

    """
    i)	Change the pixel values of the image in the following way:
    all pixels’ values less than the average value calculated at (h) will be equal to 0
    and all the other pixels will be equal to 1. Then, save it in output directory as "bicycleoutA.jpg"
    """

    bicycleoutA = np.copy(bicyclegray)

    cv2.threshold(bicyclegray, bicyclegrayAvg, 255, cv2.THRESH_BINARY, bicycleoutA)

    cv2.imshow("Question 1 i", bicycleoutA)

    cv2.imwrite("./../output/bicycleoutA.jpg", bicycleoutA)

    # j)	What type of image that is generated at (i)? What you see

    print("You see a black or white image based on if the average color is higher or lower then the average value.")

    ### END OF STUDENT CODE ####
    ############################

    cv2.waitKey(0)
    cv2.destroyAllWindows()
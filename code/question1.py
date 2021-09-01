"""
Group Number: ..........
Group Names :
     Last name , First name
     .......
     .......


"""

import cv2
import numpy as np

if __name__ == '__main__':
    ############################
    ### TODO: YOUR CODE HERE ###

    # raise NotImplementedError('Implementation for `Question ` in `workshop` is missing')
    #

    # Step 1
    hundredDollars = cv2.imread("./../data/100dollars.tif", cv2.IMREAD_GRAYSCALE)

    # Step 2
    cv2.imshow("Original Image", hundredDollars)

    # Step 3
    negativeHundredDollars = 255 - hundredDollars

    cv2.imshow("Negative Image", negativeHundredDollars)

    # Step 4
    cv2.imwrite('./../output/1_q3_100dollars_ImageNegative.tif', negativeHundredDollars)

    # Step 5
    '''
    I see an image with only the greyscale image channel in the original and negative 
    version of themselves in steps 3 and 4.
    
    Since greyscale values can only be of a value 0 - 255, all I needed to do was subtract
    255 to make the opposite or negative version of the image, which means subtracting 255
    from the greyscale value.
    '''

    # Step 6
    tire = cv2.imread("./../data/tire.tif", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Step 6 tire original image", tire)
    negativeTire = 255 - tire
    cv2.imshow("Step 6 negative image", negativeTire)
    cv2.imwrite('./../output/1_q3_tire_ImageNegative.tif', negativeTire)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ### END OF STUDENT CODE ####
    ############################

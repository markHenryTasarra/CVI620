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
    flower = cv2.imread('./../data/Flower.bmp', cv2.IMREAD_COLOR)

    # Step 2
    cv2.imshow('Step 2', flower)

    # Step 3
    FlowerHsv = cv2.cvtColor(flower, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Image', FlowerHsv)
    cv2.imwrite('./../output/FlowerHSV.jpg', FlowerHsv)

    # Step 4
    FlowerHsvH, FlowerHsvS, FlowerHsvV = cv2.split(FlowerHsv)

    cv2.imshow("H Ch", FlowerHsvH)
    cv2.imshow("S Ch", FlowerHsvS)
    cv2.imshow("V Ch", FlowerHsvV)

    cv2.imwrite('./../output/1_q2_FlowerHCh.jpg', FlowerHsvH)
    cv2.imwrite('./../output/1_q2_FlowerSCh.jpg', FlowerHsvS)
    cv2.imwrite('./../output/1_q2_FlowerVCh.jpg', FlowerHsvV)

    # Step 5
    """
    Look at Week 2/3
    What happened with the HSV is that each value in the BGR original
    image got their values directly transferred to the corresponding channel
    in the HSV destination (Blue to Hue, Green to Saturation, and red to value,
    which is why the image looks different. 
    
    When the image was split into 3 different images, each image only took 1 value of 
    the HSV image and left the rest empty (0). That is why each image looked different 
    when split, with the variations between the images being the hue, saturation, and value.

    Step 1 and 2 were self explanatory.
    
    Step 3 uses an opencv function cvtColor to convert the 
    BGR (Blue Green Red) to an HSV (Hue, saturation, value) type image. 
    
    Step 4 uses the cv2.split command to split HSV into the corresponding image objects.
    """

    # Step 6
    stepSix = np.zeros(np.shape(FlowerHsv))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ### END OF STUDENT CODE ####
    ############################

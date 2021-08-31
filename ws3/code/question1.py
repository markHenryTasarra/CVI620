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

    width = 640
    height = 480

    blank = np.zeros((width, height, 3), dtype='uint8')

    cv2.line(blank, (height // 2, 0), (height // 2, width), (0, 0, 255), 4)

    cv2.line(blank, (0, width // 2), (height, width // 2), (0, 0, 255), 4)

    cv2.imshow('Workshop 3', blank)

    cv2.imwrite("./../output/twolines.jpg", blank)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ### END OF STUDENT CODE ####
    ############################


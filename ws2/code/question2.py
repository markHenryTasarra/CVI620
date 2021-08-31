"""
Group Number: ..........
Group Names :
     Last name , First name
     .......
     .......
"""


"""
Question 2:
Reducing the Number of Intensity Levels in an Image
Write a computer program capable of reducing the number of intensity levels in a gray image from 256 levels to 2 levels,
in integer powers of 2. That is intensity levels: 256 default, 128, 64, 32, 16, 8, 4, 2.
Use image "lena.tif" from data directory
Note: Your code should generate the image with the required intensity and then write/save the image
to the output directory.
The name of generated images as following lena256.jpg, lena128.jpg, lena64.jpg, lena32.jpg, lena16.png,
 lena8.png, lena4.png, and lena2.png.




"""
import cv2
import numpy as np

if __name__ == '__main__':


    ############################
    ### TODO: YOUR CODE HERE ###

    # raise NotImplementedError('Implementation for `Question ` in `workshop2` is missing')

    lenaImg = cv2.imread("./../data/lena.tif")

    cv2.imshow('Original image', lenaImg)

    # 256 default, 128, 64, 32, 16, 8, 4, 2

    # rows, cols = lenaImg.shape

    # for i in range(rows):
    #     for j in range(cols):
    #         k = lenaImg[i, j]
    #         print(k)

    for i in range(0, lenaImg.shape[0]):
        for j in range(0, lenaImg.shape[1]):
            pixel = lenaImg.item(i, j)
            print(pixel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ### END OF STUDENT CODE ####
    ############################


"""
Group Number: ..........
Group Names :
     Last name , First name
     .......
     .......


"""

import cv2
import numpy as np

# Step 4
import matplotlib.pyplot as plt

def compute_hist_loop(img):
    freqCount = np.zeros([256], dtype='int')
    # print(freqCount.shape)
    ht, wt = img.shape # size of image
    for x in range(ht):
        for y in range(wt):
            freqCount[img[x][y]] = freqCount[img[x][y]] + 1
    return freqCount

if __name__ == '__main__':
    ############################
    ### TODO: YOUR CODE HERE ###

    # raise NotImplementedError('Implementation for `Question ` in `workshop` is missing')
    #

    # Step 1
    seagrayscale = cv2.imread("./../data/seagrayscale.jpg", cv2.IMREAD_GRAYSCALE)

    # Step 2
    cv2.imshow("Step 2", seagrayscale)

    # Step 3 - 8
    raw_hist = compute_hist_loop(seagrayscale)

    # Step 5
    fig = plt.figure(figsize=(14, 8))

    plt.bar(np.arange(len(raw_hist)), raw_hist, color='red', alpha=0.6)
    plt.title("Question 1 Step 7")
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=16))
    plt.tick_params(axis='x',labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.grid(b=True, which='major', color='#666666', linestyle='-',alpha=0.24)
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)

    # Step 8
    plt.savefig("./../output/1_q1_seagrayscale_hist.jpg", bbox_inches='tight', dpi=300)

    # Step 7
    plt.show()

    # Step 9
    hist, bins = np.histogram(seagrayscale.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    # Step 10
    fig1 = plt.figure(figsize=(14, 8))

    # Step 11
    plt.plot(cdf_normalized, color='b')
    plt.hist(seagrayscale.flatten(), 256, [0, 256], color='r')

    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=16))
    plt.tick_params(axis='x',labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-',alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.title("Question 1 Step 11")

    # Step 12
    plt.savefig("./../output/1_q1_seagrayscale_CDF.jpg", bbox_inches='tight',dpi=300)
    plt.show()

    # Step 13
    imgequ = cv2.equalizeHist(seagrayscale)
    histo = cv2.calcHist([seagrayscale], [0], None, [256], [0, 256])
    histequ = cv2.calcHist([imgequ], [0], None, [256], [0, 256])

    hist, bins = np.histogram(seagrayscale.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalizedo = cdf * hist.max() / cdf.max()
    hist, bins = np.histogram(imgequ.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalizedq = cdf * hist.max() / cdf.max()

    fig2 = plt.figure(figsize=(16, 9))

    plt.subplot(221)
    plt.imshow(seagrayscale, cmap='gray')
    plt.title('Original image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(223)
    plt.bar(np.arange(len(histo)), histo.flatten(), color='red', alpha=0.6)
    plt.plot(cdf_normalizedo, color='black')
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=32))
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=10)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.subplot(222)
    plt.imshow(imgequ, cmap='gray')
    plt.title('Equal image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(224)
    plt.bar(np.arange(len(histequ)), histequ.flatten(), color='blue', alpha=0.6)
    plt.plot(cdf_normalizedq, color='black')
    plt.title("Question 1 Step 13")
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=32))
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=10)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.savefig("./../output/1_q1_seagrayscale_eq.jpg", bbox_inches='tight', dpi=300)
    plt.show()


    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ### END OF STUDENT CODE ####
    ############################
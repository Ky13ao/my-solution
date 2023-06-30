# load the required packages
import cv2
import numpy as np

# load the image into system memory
image = cv2.imread('sample_request\\IMG_9857.jfif')

sharpen_kernel = -1/320 * np.array([[1, 4, 6, 4, 1],
                                    [4, 6, 24, 6, 4],
                                    [6, 24, -476, 24, 6],
                                    [4, 6, 24, 6, 4],
                                    [1, 4, 6, 4, 1]])
sharpen = cv2.filter2D(image, -1, sharpen_kernel)


isWritten = cv2.imwrite(
    r'C:\\testing\\sample_request\\res4.png', sharpen)


if isWritten:
    print('Image is successfully saved as file.')

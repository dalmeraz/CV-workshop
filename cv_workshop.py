#%% How to open a file
import cv2

file = "dog.jpg"
image = cv2.imread(file)
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
#%% How to open a file and make it gray scale
import cv2

def turn_image_grayscale(image):
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            pixel_average = image[r,c,0]//3 +image[r,c,1]//3 + image[r,c,2]//3
            image[r,c,0] = image[r,c,1] = image[r,c,2] = pixel_average
    return image

file = "dog.jpg"
image = cv2.imread(file)

gray_image = turn_image_grayscale(image)
cv2.imshow("image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
#%% How to open a file and make it Negative Naively
import cv2

def turn_image_negative(image):
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            image[r,c,0] = 255 - image[r,c,0]
            image[r,c,1] = 255 - image[r,c,1]
            image[r,c,2] = 255 - image[r,c,2]
    return image

file = "dog.jpg"
image = cv2.imread(file)

negative_image = turn_image_negative(image)
cv2.imshow("image", negative_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
import numpy as np
import cv2 as cv

image = cv.imread('dog.jpg')
kernel =  np.array([[1 ,1 ,1 ],[1, 1, 1],[1,1,1]])/9
blurred_image = cv.filter2D(image,-1,kernel)

cv2.imshow("image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
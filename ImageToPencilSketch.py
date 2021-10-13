# This Project converts an image to a pencil sketch

import cv2

#Get the image location and the image file name

img_loation = 'C:/Users/SURAJ/Desktop/' #You need a your Desktop image path location
filename = 'cat_image.jpg'

#Read in image
img = cv2.imread(img_loation+filename)

#Convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
invert_gray_img = 255 - gray_image

#Blur the image by gaussion function
blurred_img = cv2.GaussianBlur(invert_gray_img, (21,21), 0)

#Invert the blur image
invert_blurred_img = 255 - blurred_img

#Create the pencil sketch image
pencil_sketch_img = cv2.divide(gray_image, invert_blurred_img, scale=256.0)

#Show the image
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_img)
cv2.waitKey(0)

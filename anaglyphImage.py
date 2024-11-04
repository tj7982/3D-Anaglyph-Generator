import cv2
import numpy as np


img1 = cv2.imread("img3-l.jpg")
img2 = cv2.imread("img3-r.jpg")

rows = img1.shape[0]
cols = img1.shape[1]

anaglyphImage = np.zeros((rows, cols+10, 3), np.float32)

for i in range(rows):
    for j in range(cols):
        anaglyphImage[i,j,2] = img1[i,j,2]
        anaglyphImage[i,j+2,0] = img2[i,j,0]
        anaglyphImage[i,j+2,1] = img2[i,j,1]

cv2.imshow("Anaglyph Image", anaglyphImage/255.0)
cv2.waitKey(0)
cv2.destroyAllWindows()


# load in an image
#image = cv2.imread("birdFilter.png")
# get image dimenions
#rows = image.shape[0] # how tall image is
#cols = image.shape[1] # how wide image is
# create a new image (same size or original image)
# rgb image
#newImage = np.zeros((rows, cols, 3), np.float32) #rgb image
#grayImage = np.zeros((rows, cols, 1), np.float32) #grayscale image
#grayImage2 = np.zeros((rows, cols, 1), np.float32) #grayscale image
# iterate over all pixels
#for i in range(rows): # runs from top to bottom of image
#    for j in range(cols): # runs left to right across image
        # red channel: image[i,j,2]
        # green channel: image[i,j,1]
        # blue channel: image[i,j,0]
#        grayImage[i,j] = (float(image[i+1,j+1,0]) + float(image[i,j,1]) \
 #                         + float(image[i,j,2]))/3.0
  #      grayImage2[i,j] = 0.082*float(image[i,j,0]) + \
   #                       0.609*float(image[i,j,1]) + \
    #                      0.309*float(image[i,j,2])
        # copying red pixel from image to newImage
     #   newImage[i,j,2] = image[i,j,2]
      #  newImage[i,j,0] = image[i,j,0]
# saving an image
#cv2.imwrite("savedImage.png", grayImage2*255.0)
# display an image
#cv2.imshow("Image Display", image/255.0)
# for images you create/manipulate, scale colors down to
#[0.0, 1.0] range
#cv2.imshow("Image I Created", newImage)
#cv2.imshow("Grayscale Image", grayImage/255.0)
#cv2.imshow("Grayscale Image 2", grayImage2/255.0)
# make program halt and show image
#cv2.waitKey(0)
#have to close the window(hit x), or hit enter
#cv2.destroyAllWindows()

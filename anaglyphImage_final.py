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



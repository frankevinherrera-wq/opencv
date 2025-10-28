import cv2 as cv

img = cv.imread('imagenes/capture.png')

cv.imshow("cap", img)
cv.waitKey(0)
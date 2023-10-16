#GRAYSCALE IMAGE - BLACK AND WHITE
import cv2
img = cv2.imread('abc.jpg')
Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ORIGIONAL IMAGE',img)
cv2.imshow('GRAY SCALE IMAGE',Gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

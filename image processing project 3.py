''''import cv2
img=cv2.imread('abc.jpg')
cv2.imshow('OUTPUT1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#creating a duplicate image
import cv2
img=cv2.imread('abc.jpg')
cv2.imshow('OUTPUT1',img)
cv2.imwrite('adi.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows

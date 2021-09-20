import cv2

img=cv2.imread('../img/lena.jpg')
cv2.imshow('lenna',img)
cv2.waitKey()
cv2.destroyAllWindows()
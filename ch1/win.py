import cv2

file_path='../img/girl.jpg'

img=cv2.imread(file_path)
img_gray=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('origin',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('gray',cv2.WINDOW_NORMAL)

cv2.imshow('origin',img)
cv2.imshow('gray',img_gray)
cv2.waitKey()

cv2.moveWindow('origin',0,0)
cv2.moveWindow('gray',200,200)

cv2.resizeWindow('origin',100,100)
cv2.resizeWindow('gray',300,300)

cv2.waitKey()
cv2.destroyAllWindows()

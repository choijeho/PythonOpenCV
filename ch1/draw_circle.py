import cv2
import numpy as np
img=cv2.imread('../img/blank_500.jpg')
center=(200,200)
ellipseshape=(100,20)
color=(255,0,0)
cv2.ellipse(img,center,ellipseshape,0,0,360,color,-1,cv2.LINE_AA)
cv2.imshow('draw',img)
cv2.waitKey()
cv2.destroyAllWindows()
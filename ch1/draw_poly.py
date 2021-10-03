import cv2
import numpy as np
img=cv2.imread('../img/blank_500.jpg')
points=np.array([[10,10],[10,50],[50,50],[50,10]])
color=(255,0,0)
cv2.polylines(img,[points],True,color,10,cv2.LINE_AA)
cv2.imshow('draw',img)
print(points)
print([points])
cv2.waitKey()
cv2.destroyAllWindows()
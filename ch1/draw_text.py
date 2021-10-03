import cv2

img=cv2.imread('../img/blank_500.jpg')

color=(255,0,0)

cv2.putText(img,"plain",(100,100),cv2.FONT_HERSHEY_SIMPLEX,3,color,2)

cv2.imshow('draw',img)
cv2.waitKey()
cv2.destroyAllWindows()
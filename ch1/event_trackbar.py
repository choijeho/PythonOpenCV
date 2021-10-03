import cv2
import numpy as np

title='Trackbar'
img=cv2.imread('../img/blank_500.jpg')
cv2.imshow(title,img)

def onChange(x):
    print(x)
    r=cv2.getTrackbarPos('R',title)
    g=cv2.getTrackbarPos('G',title)
    b=cv2.getTrackbarPos('B',title)
    print(r,g,b)
    img[:]=[b,g,r]
    cv2.imshow(title,img)


cv2.createTrackbar('R',title,0,255,onChange)
cv2.setTrackbarPos('R',title,)
cv2.createTrackbar('G',title,0,255,onChange)
cv2.createTrackbar('B',title,0,255,onChange)

while True:
    if cv2.waitKey(1)&0xff==27:
        break

cv2.destroyAllWindows()
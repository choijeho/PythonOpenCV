import cv2

title='mouse event'
img=cv2.imread('../img/blank_500.jpg')
cv2.imshow(title,img)

def onMouse(event,x,y,flags,param):
    print(event,x,y)
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),30,(255,0,0),-1)
        cv2.imshow(title,img)

cv2.setMouseCallback(title, onMouse)
while True:
    if cv2.waitKey(0)&0xff==27:
        break
cv2.destroyAllWindows()
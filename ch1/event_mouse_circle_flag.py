import cv2

title='color dots'
img=cv2.imread('../img/blank_500.jpg')
cv2.imshow(title,img)
colors={'black':(0,0,0),
        'red':(0,0,255),
        'blue':(255,0,0),
        'green':(0,255,0)}

def onMouse(event,x,y,flag,param):
    print(event,x,y)
    color=colors['black']
    if event==cv2.EVENT_LBUTTONDOWN:
        if flag&cv2.EVENT_FLAG_CTRLKEY and flag&cv2.EVENT_FLAG_SHIFTKEY:
            color=colors['green']
        elif flag&cv2.EVENT_FLAG_SHIFTKEY:
            color=colors['blue']
        elif flag&cv2.EVENT_FLAG_CTRLKEY:
            color=colors['red']
        cv2.circle(img,(x,y),30,color,-1)
        cv2.imshow(title,img)

cv2.setMouseCallback(title,onMouse)
while True:
    if cv2.waitKey(0)&0xff==27:
        break

cv2.destroyAllWindows()
import cv2

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
if cap.isOpened():
    width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("Width: %d, Height: %d"%(width,height))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
    width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("Width: %d, Height: %d"%(width,height))
    while True:
        ret,img=cap.read()
        if ret:
            cv2.imshow('cam',img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
else:
    print('no camera available')
cap.release()
cv2.destroyAllWindows()
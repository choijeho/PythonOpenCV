import cv2

vf='../img/big_buck.avi'

cap=cv2.VideoCapture(vf)
if cap.isOpened():
    fps=cap.get(cv2.CAP_PROP_FPS)
    delay=int(1000/fps)
    print("FPS: %f, Delay: %dms" % (fps,delay))

    while True:
        ret,img=cap.read()
        if ret:
            cv2.imshow('video',img)
            cv2.waitKey(delay)
        else:
            break
else:
    print('no video')
cap.release()
cv2.destroyAllWindows()
import cv2

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
if cap.isOpened():
    file_path="../img/movrec.avi"
    fourcc=cv2.VideoWriter_fourcc(*"DIVX")
    fps=25.4
    width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size=(int(width),int(height))
    vidout=cv2.VideoWriter(file_path, fourcc, fps, size)
    while True:
        ret,img=cap.read()

        if ret:
            cv2.imshow('cam',img)
            vidout.write(img)
            if cv2.waitKey(1)!=-1:
                break
        else:
            print('no frame')
else:
    print('no camera')
cap.release()
cv2.destroyAllWindows()
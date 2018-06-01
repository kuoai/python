import numpy as np
import cv2
def getFace(image):
    # cvo = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    # cvo.load("C:\Python36\opencv\haarcascades\haarcascade_frontalface_default.xml")

    cvo = cv2.CascadeClassifier(r'C:\Python36\opencv\haarcascades\haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = cvo.detectMultiScale(
        gray,
        scaleFactor= 1.15,
        minNeighbors= 5,
        minSize= (5,5),
        # flags= cv2.HAAR_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)

# 开启摄像头，一般笔记本默认为0
cam = cv2.VideoCapture(0)
# 获取摄像头输出视频的长度
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
# 定义编码
fourcc = cv2.VideoWriter_fourcc(*"mp4v")            #定义编码
# out = cv2.VideoWriter("test.mp4",fourcc,20.0,(width,height))
out = cv2.VideoWriter('test.mp4', fourcc, 20.0, (640,480))
while(cam.isOpened()):
    # 读取帧摄像头
    ret,frame = cam.read()
    if ret == True:
        # frame = getFace(frame)      #获取得的值传入我们定义的getFace函数中处理
        out.write(frame)
        cv2.imshow('window', frame)
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            break
    else:
        break
out.release()
cam.release()
cv2.destroyAllWindows()
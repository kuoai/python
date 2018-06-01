import sys
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc('H','2','6','4')

cap.set(6, fourcc)
cap.set(3,1920)
cap.set(4,1080)
cap.set(5, 30)

vid = cv.VideoWriter('test1.mp4', fourcc, 20.0, (640,480))
print(vid.isOpened()) #returns false :(
while (cap.isOpened()):

  ret, frame = cap.read()

  if (ret == True):

   #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


   vid.write(frame)

   cv.imshow('window', frame)

   if (cv.waitKey(1) & 0xFF == ord('q')):
    break

cap.release()
vid.release()
cv.destroyWindow('window')
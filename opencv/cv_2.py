import cv2
# Haar-like     Haar特征值反映了图像的灰度变化情况,脸部的一些特征能由矩形特征简单的描述，
# 如：眼睛要比脸颊颜色要深，鼻梁两侧比鼻梁颜色要深，嘴巴比周围颜色要深等
# opencv api    要想使用opencv，就必须先知道其能干什么，怎么做。于是API的重要性便体现出来了。
# 就本例而言，使用到的函数很少，也就普通的读取图片，灰度转换，显示图像，简单的编辑图像罢了

imagepath = "more.jpg"      #待检测的图片
image = cv2.imread(imagepath)       #读取图片

# 灰度转换的作用就是：转换成灰度的图片的图片强度得以降低
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)   #灰度转换

# 获取人脸识别的数据
face_cascade = cv2.CascadeClassifier(r'C:\Python36\opencv\haarcascades\haarcascade_frontalface_default.xml')

# 探测人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.15,
    minNeighbors= 5,
    minSize= (5,5),
    # flags= cv2.HAAR_SCALE_IMAGE
)

# 我们可以随意的制定里面参数的值，来达到不同精度下的识别
# 返回值就是poencv对图片的探索结果的体现

# 处理人脸检测的结果
print("发现了{0}个人脸".format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,0,0),2)

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
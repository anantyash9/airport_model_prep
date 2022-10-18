import numpy
import cv2
img = numpy.zeros([350*8,350*8,3])

for x in range(8):
    for y in range(8):
        if (x+y)%2==0:
            print(x,y)
            print(img[x*350:(x+1)*350,y*350:(y+1*350),0].shape)
            img[x*350:(x+1)*350,y*350:(y+1)*350,0] = numpy.ones([350,350])*255
            img[x*350:(x+1)*350,y*350:(y+1)*350,1] = numpy.ones([350,350])*255
            img[x*350:(x+1)*350,y*350:(y+1)*350,2] = numpy.ones([350,350])*255

cv2.imwrite("img.png",img)
cv2.imshow("image", img)
cv2.waitKey()
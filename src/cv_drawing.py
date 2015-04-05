#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Created by 'quanpower' on '15-4-5'
#Email:quanpower@gmail.com
#QQ:252527676
#Site:www.smartlinkcloud.com

__author__ = 'quanpower'

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.circle(img,(447,63),63,(0,0,255),-1)
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,255),-1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'smartlinkcloud',(10,500),font,4,(255,255,255),2)
#img = cv2.putText(img,'smartlinkcloud',(10,500),font,4,(255,255,255),2)
#***************this has problem in opencv 2.4.9 on ubuntu 14.04***********

winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
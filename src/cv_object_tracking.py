#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Created by 'quanpower' on '15-4-9'
#Email:quanpower@gmail.com
#QQ:252527676
#Site:www.smartlinkcloud.com

__author__ = 'quanpower'

import cv2
import numpy as np

img = cv2.imread("../files/object1.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#define color in green color in HSV
lower_green = np.array([60,40,40])
uper_green = np.array([100,255,255])

mask = cv2.inRange(hsv,lower_green,uper_green)

res = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow('hsv',hsv)
cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.waitKey(0)

cv2.destroyAllWindows()



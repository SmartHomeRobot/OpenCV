#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Created by 'quanpower' on '15-4-5'
#Email:quanpower@gmail.com
#QQ:252527676
#Site:www.smartlinkcloud.com

__author__ = 'quanpower'

import cv2
import numpy as np

img = cv2.imread('../files/img_test.jpg')
px = img[100,100]
print px

blue = img[100,100,0]
print blue

img[100,100] = [255,255,255]
print img[100,100]

red = img.item(10,10,2)
print red

img.itemset((10,10,2),255)
red1= img.item(10,10,2)
print red1

print img.shape
print img.size
print img.dtype

tree = img[100:200,400:500]
img[200:300,500:600] = tree

b = img[:,:,0]
img[:,:,1] = 0
g = img.item(100,100,1)
print g

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Created by 'quanpower' on '15-4-4'
#Email:quanpower@gmail.com
#QQ:252527676
#Site:www.smartlinkcloud.com

__author__ = 'quanpower'

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('index.jpeg')

#b,g,r = cv2.split(img)
#img2 = cv2.merge([r,g,b])

img2 = img[:,:,::-1] #more simple

plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()

#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Created by 'quanpower' on '15-4-4'
#Email:quanpower@gmail.com
#QQ:252527676
#Site:www.smartlinkcloud.com

__author__ = 'quanpower'

import numpy as np
import cv2

img = cv2.imread('img_test.jpg',0)
cv2.namedWindow('sea',cv2.WINDOW_NORMAL)
cv2.imshow('sea',img)
k = cv2.waitKey(0)&0xFF # for 64bit pc
if k == 27:
    cv2.destroyAllWindows() #Wait for 'esc' key to exit
elif k == ord('s'):         #Wait for 's' key to save and exit
    cv2.imwrite('sea1.png',img)
    cv2.destroyAllWindows()
#!/usr/bin/python
# -*- encoding: utf-8 -*-

#Created by 'quanpower' on '15-4-4'
#Email:quanpower@gmail.com
#QQ:252527676
#Site:www.smartlinkcloud.com

__author__ = 'quanpower'

import numpy as np
import cv2

#获得视频的格式
videoCapture =cv2.VideoCapture('../files/video_test2.avi')

#获得码率及尺寸
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
print(fps) #this video have problem,return fps:nan
fps = 1000 #usually 25,set 1000 for write faster

size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

#指定写视频的格式, I420-avi, MJPG-mp4
videoWriter = cv2.VideoWriter('oto_other.mp4', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)

#读帧
success, frame = videoCapture.read()

while success:
    cv2.imshow('Oto Video', frame) #显示
    cv2.waitKey(1000/int(fps)) #延迟
    videoWriter.write(frame) #写视频帧
    success, frame = videoCapture.read() #获取下一帧

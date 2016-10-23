import cv2
import os
import numpy as np

from os import listdir
from os.path import isfile, join
cap = cv2.VideoCapture("/home/atanu/Desktop/Soccer2.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("/home/atanu/Desktop/Soccer2.mp4")
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
while True:
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        cv2.imshow('video', frame)
        cv2.imwrite("/home/atanu/PycharmProjects/lab6/frames/img%02d.jpg" %pos_frame,frame)

        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        #print str(pos_frame)+" frames"

    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        print "frame is not ready"
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break
    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break

#applying sift features
#file_list = os.listdir(r"/home/atanu/PycharmProjects/lab6/frames/")
file_list = "/home/atanu/PycharmProjects/lab6/frames/"
onlyfiles = [ f for f in listdir(file_list) if isfile(join(file_list,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(file_list,onlyfiles[n]) )

  gray = cv2.cvtColor(images[n], cv2.COLOR_BGR2GRAY)
  sift = cv2.SIFT()
  kp = sift.detect(gray, None)

  img = cv2.drawKeypoints(gray, kp)

  cv2.imwrite('/home/atanu/PycharmProjects/lab6/siftframes/sift_keypoints%d.jpg' %n, img)
  cv2.imshow('sift_keypoints%d.jpg' %n, img)

  # gray = cv2.cvtColor()
#for file_name in file_list:
    #img = cv2.cv.LoadImage('/home/atanu/PycharmProjects/lab6/frames/img00.jpg')
    #img = cv2.VideoCapture('/home/atanu/PycharmProjects/lab6/frames/img%02d.jpg')




    #print img
    #ig = np.asarray(img)
    #gray=cv2.cvtColor(ig,cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor()
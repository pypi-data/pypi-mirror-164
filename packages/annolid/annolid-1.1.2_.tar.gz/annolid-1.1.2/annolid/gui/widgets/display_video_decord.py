import decord as de
import numpy as np
import cv2

VIDEO_PATH = "/Users/chenyang/Downloads/First_wild_foal_of_the_season-Lq_ylLQn8P8.mp4"
de.bridge.set_bridge('native')
vr = de.VideoReader(VIDEO_PATH, ctx=de.cpu(0))
num_frames = range(len(vr))


frame = (vr[0].asnumpy())
cv2.imshow('video', frame)
cv2.waitKey(0)

import itertools
import cv2
import os
import numpy as np
import glob

#User defined variables
dirname = "/Users/chenyang/Downloads/HighF-07_6000_6300_tracked" #Name of the directory containing the images
name = "tracking_three_voles_across_frames" + ".jpg" #Name of the exported file
margin = 20 #Margin between pictures in pixels
w = 4 # Width of the matrix (nb of images)
h = 10 # Height of the matrix (nb of images)
n = w*h

images_files = glob.glob(f"{dirname}/*.jpg")
imgs = []
for img in sorted(images_files):
    bgr_img = cv2.imread(img)
    rgb_img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2RGB)
    imgs.append(rgb_img)

#Define the shape of the image to be replicated (all images should have the same shape)
img_h, img_w, img_c = imgs[0].shape

#Define the margins in x and y directions
m_x = margin
m_y = margin

#Size of the full size image
mat_x = img_w * w + m_x * (w - 1)
mat_y = img_h * h + m_y * (h - 1)

#Create a matrix of zeros of the right size and fill with 255 (so margins end up white)
imgmatrix = np.zeros((mat_y, mat_x, img_c),np.uint8)
imgmatrix.fill(255)

#Prepare an iterable with the right dimensions
positions = itertools.product(range(h), range(w))

for (y_i, x_i), img in zip(positions, imgs):
    x = x_i * (img_w + m_x)
    y = y_i * (img_h + m_y)
    imgmatrix[y:y+img_h, x:x+img_w, :] = img

resized = cv2.resize(imgmatrix, (mat_x//3,mat_y//3), interpolation = cv2.INTER_AREA)
compression_params = [cv2.IMWRITE_JPEG_QUALITY, 90]
cv2.imwrite(name, resized, compression_params)
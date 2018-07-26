import os, glob
import cv2
ulpath = r"C:\Users\wangy\models\research\deeplab\datasets\pascal_voc_seg\VOCdevkit\VOC2012\SegmentationClass"
import numpy as np
for infile in glob.glob( os.path.join(ulpath, "*.png") ):
	im = cv2.imread(infile)
	height, width, channels = im.shape
	maxdim = max(height, width)
	if(maxdim > 500):
		resizefactor = 500/maxdim
		small = cv2.resize(im, (0,0), fx=resizefactor, fy=resizefactor)
		cv2.imwrite(infile, small)
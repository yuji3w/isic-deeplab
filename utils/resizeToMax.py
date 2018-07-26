import os, glob
import cv2
ulpath = r"C:\Users\Yujie Wang\Desktop\testfolder"
import numpy as np
for infile in glob.glob( os.path.join(ulpath, "*.png") ):
	im = cv2.imread(infile)
	height, width, channels = im.shape
	small = cv2.resize(im, (0,0), fx=513/width, fy=513/height)
	cv2.imwrite(infile, small)
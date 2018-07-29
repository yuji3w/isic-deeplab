import os, glob
import cv2
from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="myInput", help="input directory")
args = parser.parse_args()
myInput = args.myInput
ulpath = myInput

print(ulPath)

for infile in glob.glob( os.path.join(ulpath, "*.png") ):
	im = cv2.imread(infile)
	height, width, channels = im.shape
	maxdim = max(height, width)
	if(maxdim > 500):
		resizefactor = 500/maxdim
		small = cv2.resize(im, (0,0), fx=resizefactor, fy=resizefactor)
		cv2.imwrite(infile, small)
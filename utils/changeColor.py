import cv2
import os
import numpy as np

gtFolder = r"C:\Users\wangy\Desktop\changeColor"


for root, dirs, files in os.walk(gtFolder):
	for file in files:
		if file.endswith('.png'):
			path = os.path.join(gtFolder,file)
			im = cv2.imread(path)
			im[np.where((im != [0,0,0]).all(axis = 2))] = [0,0,128]
			cv2.imwrite(path, im)
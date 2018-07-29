import cv2
import os
import statistics

gtFolder = r"C:\Users\isica\Desktop\gt" #UPDATE PATHS -----
predFolder = r"C:\Users\isica\Desktop\predict"


def pixelComp(firstPath,secondPath):
	firstImg = cv2.imread(firstPath,cv2.IMREAD_GRAYSCALE)
	secondImg = cv2.imread(secondPath,cv2.IMREAD_GRAYSCALE)
	height, width = firstImg.shape
	blackRed = blackBlack = whiteRed = whiteBlack = 0
	for y in range(0, height):
		for x in range(0, width):
			firstCol = firstImg.item(y,x)
			secondCol = secondImg.item(y,x)
			if firstCol==0:
				if secondCol==0:
					blackBlack += 1
				else:
					blackRed += 1
					
			else:
				if secondCol==0:
					whiteBlack += 1
				else:
					whiteRed +=1

	return blackRed, blackBlack, whiteRed, whiteBlack

def jaccard(bb, br, wb, wr):
	# Assuming foreground is red
	intersection = wr
	union = wr + wb + br

	return float(intersection) / union

count = valid = 0
jVals = []
for root, dirs, files in os.walk(predFolder):
	for file in files:
		if file.endswith('prediction.png'):
			firstPath = os.path.join(gtFolder,file)
			secondPath = os.path.join(predFolder,file)
			print(firstPath)
			tblackRed, tblackBlack, twhiteRed, twhiteBlack = pixelComp(firstPath,secondPath)
			
			print(tblackRed)
			print(tblackBlack)
			print(twhiteRed)
			print(twhiteBlack)

			j = jaccard(tblackBlack, tblackRed, twhiteBlack, twhiteRed)
			print(j)
			jVals.append(j)
			count += 1
			if j >= 0.65:
				valid += 1
				
if count > 0:
	print("MEAN JACCARD VALUE = " + str(statistics.mean(jVals)))
	print("MEDIAN JACCARD VALUE = " + str(statistics.median(jVals)))
	print("STD DEVIATION = " + str(statistics.pstdev(jVals)))
	print(str(valid) + " VALID SEGMENTATIONS OF " + str(count) + " = " + str(float(valid) / count))
else:
	print("NO IMAGES FOUND")
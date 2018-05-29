from collections import namedtuple
import pandas as pd
import numpy as np
import detector
import cv2
import csv

def eval(boxA, boxB):
	xA = max(int(boxA[0]), int(boxB[0]))
	yA = max(int(boxA[1]), int(boxB[1]))
	xB = min(int(boxA[2]), int(boxB[2]))
	yB = min(int(boxA[3]), int(boxB[3]))

	interArea = (xB - xA + 1) * (yB - yA + 1)

	boxAArea = (int(boxA[2]) - int(boxA[0]) + 1) * (int(boxA[3]) - int(boxA[1]) + 1)
	boxBArea = (int(boxB[2]) - int(boxB[0]) + 1) * (int(boxB[3]) - int(boxB[1]) + 1)

	iou = interArea / float(boxAArea + boxBArea - interArea)

	return iou


def evaluate():
	count = 0
	sumscore = 0
	with open('labels.csv', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for data in reader:
			filename = data[0]
			detect_coords = detector.detect(filename)
			actual_coords = [data[1],data[2],data[3],data[4]]
			score = eval(actual_coords, detect_coords)

			# Printing IoU scores
			sumscore += score
			count += 1
			print("File: "+filename+"\t\tIoU Score: "+str(score)+"\t\tAverage: "+str((sumscore)/(count)))

if __name__ == "__main__":

	evaluate()
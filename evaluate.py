from collections import namedtuple
import numpy as np
import cv2
import detector
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

if __name__ == "__main__":

	eval(boxA, boxB)
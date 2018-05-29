from collections import namedtuple
import pandas as pd
import numpy as np
import detector
import cv2
import csv

def evaluate():
	with open('labels.csv', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for data in reader:
			filename = data[0]
			actual_coords = [data[1],data[2],data[3],data[4]]
		
			actual_x1 = int(actual_coords[0])
			actual_y1 = int(actual_coords[1])
			actual_x2 = int(actual_coords[2])
			actual_y2 = int(actual_coords[3])

			# loop over the cat faces and draw a rectangle surrounding each
			image = cv2.imread(filename,0)
			print(filename)
			cv2.rectangle(image, (actual_x1, actual_y1), (actual_x2, actual_y2), (0, 0, 255), 2)
			# cv2.putText(image, "IOU: {}%".format(round(score,4) * 100), (min(actual_x1, detect_x1), min(actual_y1,detect_y1) - 10),
			# 	cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
			cv2.putText(image, "Cat", (actual_x1, actual_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

			# show the detected cat faces
			cv2.imshow("Cat", image)
			cv2.waitKey(0)

if __name__ == "__main__":

	evaluate()
import pandas as pd
import detector
import evaluate
import csv
import cv2
import sys 



if __name__ == "__main__":
	
	with open('labels.csv', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for data in reader:
			filename = data[0]
			detect_coords = detector.detect(filename)
			actual_coords = [data[1],data[2],data[3],data[4]]
			score = evaluate.eval(actual_coords, detect_coords)
		
			actual_x1 = int(actual_coords[0])
			actual_y1 = int(actual_coords[1])
			actual_x2 = int(actual_coords[2])
			actual_y2 = int(actual_coords[3])

			detect_x1 = int(detect_coords[0])
			detect_y1 = int(detect_coords[1])
			detect_x2 = int(detect_coords[2])
			detect_y2 = int(detect_coords[3])

			# loop over the cat faces and draw a rectangle surrounding each
			image = cv2.imread(filename)
			cv2.rectangle(image, (actual_x1, actual_y1), (actual_x2, actual_y2), (0, 255, 0), 2) # CORRECT BOUNDING BOX
			cv2.rectangle(image, (detect_x1, detect_y1), (detect_x2, detect_y2), (0, 0, 255), 2) # PREDICTED BOUNDING BOX
			cv2.putText(image, "IOU: {}%".format(round(score,4) * 100), (min(actual_x1, detect_x1), min(actual_y1,detect_y1) - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

			# show the detected cat faces
			cv2.imshow("Cat Faces", image)
			cv2.waitKey(0)
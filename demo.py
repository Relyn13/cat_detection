import pandas as pd
import csv
import cv2
import sys 

# FOR EVALUATE.PY
def detect(filename):
	# load the input image and convert it to grayscale
	image = cv2.imread(filename)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# load the cat detector Haar cascade, then detect cat faces
	# in the input image
	detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
	rects = detector.detectMultiScale(gray, scaleFactor=1.3,
		minNeighbors=10, minSize=(75, 75))

	x1=0
	y1=0
	x2=0
	y2=0

	# loop over the cat faces and draw a rectangle surrounding each
	for (i, (x, y, w, h)) in enumerate(rects):
		x1 = x
		y1 = y
		x2 = x+w
		y2 = y+h

	coords = [x1, y1, x2, y2]
	return (coords)

def evaluate(boxA, boxB):
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
	count = 0
	sumscore = 0
	with open('labels.csv', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for data in reader:
			filename = data[0]
			detect_coords = detect(filename)
			actual_coords = [data[1],data[2],data[3],data[4]]
			score = evaluate(actual_coords, detect_coords)
		
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

			# Printing IoU scores
			sumscore += score
			count += 1
			print("File: "+filename+"\tIoU Score: "+str(score)+"\tAverage: "+str((sumscore)/(count)))

			# show the detected cat faces
			cv2.imshow("Cat Faces", image)
			cv2.waitKey(0)
import argparse
import cv2
import csv
import os.path
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

def detects(filename):
	# load the input image and convert it to grayscale
	image = cv2.imread(filename)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# load the cat detector Haar cascade, then detect cat faces
	# in the input image
	detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
	rects = detector.detectMultiScale(gray, scaleFactor=1.3,
		minNeighbors=10, minSize=(75, 75))

	# loop over the cat faces and draw a rectangle surrounding each
	for (i, (x, y, w, h)) in enumerate(rects):
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
		cv2.putText(image, "Cat", (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
	 
	# show the detected cat faces
	cv2.imshow("Cat Faces", image)
	cv2.waitKey(0)


if __name__ == "__main__":

	# usage:	python detector.py <image_path>
	detects(sys.argv[1])
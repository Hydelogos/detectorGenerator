from PIL import Image
import glob
import dlib
import cv2
import numpy as np
import sys

image_list = []
boxes = []

def getImages():
	[image_list.append(cv2.cvtColor(cv2.imread(item),cv2.COLOR_BGR2RGB)) for i in [glob.glob('img/*.%s' % ext) for ext in ["jpg","png"]] for item in i]

def getBox():
	for image in image_list:
		r = cv2.selectROI(image, False)
		print(r)
		(x,y,xb,yb) = [r[0],r[1],r[0] + r[2], r[1] + r[3]]
		boxes.append([dlib.rectangle(left=int(x),top=int(y),right=int(xb),bottom=int(yb))])
	print(boxes)

def generate():
	options = dlib.simple_object_detector_training_options()
	options.add_left_right_image_flips = True
	options.num_threads = 3
	detector = dlib.train_simple_object_detector(image_list, boxes, options)
	detector.save("detector/" + sys.argv[1])
	

def test():
	detector = dlib.simple_object_detector("detector/" + sys.argv[1])
	testList = []
	[testList.append(cv2.cvtColor(cv2.imread(item),cv2.COLOR_BGR2RGB)) for i in [glob.glob('testImg/*.%s' % ext) for ext in ["jpg","png"]] for item in i]
	for image in testList:
		detectedBoxes = detector(image)
		print(detectedBoxes)
		finalBoxes = []
		for detectedBox in detectedBoxes:
			(x,y,xb,yb) = [detectedBox.left(),detectedBox.top(),detectedBox.right(),detectedBox.bottom()]
			finalBoxes.append((x,y,xb, yb))
		image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
		for finalBox in finalBoxes:
			(x,y,xb,yb) = finalBox
			cv2.rectangle(image,(x,y),(xb,yb),(0,0,255),2)
		cv2.imshow("Detected",image)
		cv2.waitKey(0)


getImages()
getBox()
generate()
test()
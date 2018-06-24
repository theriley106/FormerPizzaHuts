import glob
import cv2

def viewImage(fileName, titleBar="Is there a Pizza Hut in the image?"):
	# Opens up an image, and accepts keystrokes
	# Return keystroke must be compared with ord('key')
	# Titlebar is the text displayed at the top of the image container
	img = cv2.imread(fileName)
	# Creates image object
	cv2.imshow(titleBar, img)
	# Open up image in a new window
	keyStroke = cv2.waitKey()
	# Waits for and records a keystroke
	return keyStroke



for file in glob.glob("PizzaHuts/*"):
	keyStroke = viewImage(file)
	if keyStroke == ord('s'):
		print file

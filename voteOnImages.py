import cv2
import glob
import os
import shutil

allFiles = sorted(glob.glob("BulkImages/*/"), key=os.path.getmtime)
SAVE_TO = ""

def saveImage(fileName, saveToFolder="goodImages"):
	if not os.path.exists(saveToFolder):
		# Checks to see if the specified path exists
		os.makedirs(saveToFolder)
		# Creates a folder
	path = os.path.dirname(fileName)
	# Extracts path from filename
	addressName = os.path.basename(path)
	# Extracts address from file name
	cameraOrientation = os.path.basename(fileName)
	# Extracts camera orientation from file name
	if not os.path.exists("{}/{}".format(saveToFolder, addressName)):
		# Checks to see if an address folder exists
		os.makedirs("{}/{}".format(saveToFolder, addressName))
		# Creates address folder if it doesn't exist
	shutil.copyfile(fileName, "{}/{}/{}".format(saveToFolder, addressName, cameraOrientation))
	# Copies file to new folder

def returnAll(folderName="PizzaHuts"):
	# Returns a Python list containing all items/folder in a folder
	# Images are sorted by creation time
	return sorted(glob.glob("{}/*".format(folderName)), key=os.path.getmtime)

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

def genFileName(address, cameraTilt):
	# Generates file names
	return "{}/{}.jpg".format(address, cameraTilt)

for address in returnAll("PizzaHutBulkImages"):
	# Iterates through all addresses in PizzaHuts/
	try:
		# Try/Catch just in case there is an error
		cameraTilt = list(range(0, 340, 20))
		# This contains all camera tilt orientations in the Google Car
		currentOrientation = cameraTilt[0]
		while True:
			fileName = genFileName(address, currentOrientation)
			# Filename for this specific camera orientation
			keyChoice = viewImage(fileName)
			# Keychoice is the key a user presses in the image window
			if keyChoice == ord('n'):
				# The user inputted the letter N
				newTilt = cameraTilt.index(currentOrientation) + 1
				if newTilt == len(cameraTilt):
					# This is going to refresh the orientation from 320+ to 0
					# ^ This allows for a smoothless transition between images
					newTilt = 0
				currentOrientation = cameraTilt[newTilt]
				# Sets new orientation
			if keyChoice == ord("p"):
				# The user inputted the letter P
				currentOrientation = cameraTilt[cameraTilt.index(currentOrientation) - 1]
				# Sets new orientation
			if keyChoice == ord("q"):
				# The user inputted the letter Q
				# This indicates that this image did not have a Pizza hut
				break
				# Quits the while loop
			if keyChoice == ord("s"):
				# The user inputted the letter S
				# This indicates the user wants to save on the current image
				saveImage(fileName)
				# Saves the image
				break
				# Quits the while loop
			print("{} IN LOOP {}".format(currentOrientation, fileName))
			# Prints out information about the image
	except Exception as exp:
		print exp
		# Prints actual exception


for folder in allFiles:
	try:
		save = True
		i = 0
		e = i
		print folder
		file = folder + str(i) + ".jpg"
		currentFileName = file
		img = cv2.imread(file)
		print file
		cv2.imshow("Is there a Pizza Hut in the image?", img)
		while True:
			k = cv2.waitKey()
			if k == ord('p'):
				e = e - 1
				fileName = folder + str(list(range(0, 360, 20))[e]) + ".jpg"
				try:
					cv2.imshow("Is there a Pizza Hut in the image?", cv2.imread(fileName))
					currentFileName = fileName
				except:
					print("End of options")
					cv2.imshow("Is there a Pizza Hut in the image?", cv2.imread(folder + "0.jpg"))
					e = 0
					currentFileName = folder + "0.jpg"
			if k == ord('n'):
				e = e + 1
				fileName = folder + str(list(range(0, 360, 20))[e]) + ".jpg"
				try:
					cv2.imshow("Is there a Pizza Hut in the image?", cv2.imread(fileName))
					currentFileName = fileName
				except:
					print("End of options")
					cv2.imshow("Is there a Pizza Hut in the image?", cv2.imread(folder + "0.jpg"))
					e = 0
					currentFileName = folder + "0.jpg"
			if k == ord('s'):
				break
			if k == ord('q'):
				save = False
				break
		if save != False:
			saveImage(currentFileName)
		if save == False:
			fileName = currentFileName
			tempFolder = fileName.partition("BulkImages/")[2].partition("/")[0]
			tempFileName = fileName[::-1].partition("/")[0][::-1]
			os.system("rm -rf BulkImages/{}".format(tempFolder))
	except:
		print("ERROR")

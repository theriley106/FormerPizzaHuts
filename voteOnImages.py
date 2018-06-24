import cv2
import glob
import os
import shutil
import random
PROXIES = {}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{}.0.2171.95 Safari/537.36'.format(random.randint(1, 99))}
GOOGLE_STREETVIEW_API = "http://geo1.ggpht.com/cbk?panoid={0}&output=thumbnail&cb_client=search.LOCAL_UNIVERSAL.gps&thumb=2&w=2000&h=2000&yaw={2}&pitch=0&thumbfov=100"

allFiles = sorted(glob.glob("BulkImages/*/"), key=os.path.getmtime)
SAVE_TO = ""


def grabSite(url):
	# Makes network requests that are *ideally* not blocked by Google
	for i in range(3):
		# Tries it 3 times
		try:
			return requests.get(url, headers=HEADERS, proxies=PROXIES, timeout=10)
			# Returns the content of the site
		except Exception as exp:
			pass

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

def generateRandomCameraOrientations(cameraOrientation, rangeVal=1):
	# Returns a "Random" camera orientations
	# This is to prevent against bot detection
	# Google will ban requests if it's a constant Tilt #
	# So this would change 320 into 320.124
	return round(cameraOrientation + random.uniform(0, rangeVal), 5)

def genListOfCameraOrientations():
	# Returns a list of camera angles - Randomized using the above function
	return [generateRandomCameraOrientations(val) for val in range(0, 340, 20)]

def grabPanoidFromHTML(page):
	# Pulls a Google image Panoid string from a bs4 page object
	try:
		return str(page).partition("panoid=")[2].partition('&')[0]
		# In the future change this to regex...
	except:
		# This means there is not a Panoid
		return

def grabImagesFromAddress(address):
	imageList = []
	# Contains a list of image URLs
	addressURL = address.replace(" ", "+")
	# Converts address to a valid URL address
	url = "https://www.google.com/maps/place/" + addressURL
	# Gens URL for this address
	res = grabSite(url)
	# Pulls the url that was previously defined
	page = bs4.BeautifulSoup(res.text, 'lxml')
	# Converts it into a BS4 Object
	panoidVal = grabPanoidFromHTML(page)
	# This grabs the Panoid val from that address
	if panoidVal != None:
		# This means the address did exist
		for cameraOrientationVal in genListOfCameraOrientations():
			# Iterates through all possible camera orientations
			imageList.append(GOOGLE_STREETVIEW_API.format(panoidVal, cameraOrientationVal))
			# Appends them to the list of images
		return imageList

def downloadImage(url, saveAs):
	# Downloads an image from the internet
	response = requests.get(url, stream=True)
	# Pulls this image and saves as a requests object
	with open(saveAs, 'wb') as out_file:
		# Saves locally
	    shutil.copyfileobj(response.raw, out_file)
	del response






if __name__ == '__main__':
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

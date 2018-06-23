import cv2
import glob
import os
cv2.namedWindow("Is there a Pizza Hut in the image?")
allFiles = sorted(glob.glob("BulkImages/*/"), key=os.path.getmtime)
SAVE_TO = ""

def saveImage(fileName):
	tempFolder = fileName.partition("BulkImages/")[2].partition("/")[0]
	tempFileName = fileName[::-1].partition("/")[0][::-1]
	os.system("mkdir /home/christopher/allImages/{}".format(tempFolder))
	os.system("mv {} /home/christopher/allImages/{}/{}".format(fileName, tempFolder, tempFileName))
	os.system("rm -rf BulkImages/{}".format(tempFolder))


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

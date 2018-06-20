import json
import os
import requests
import shutil

if __name__ == '__main__':
	a = json.load(open("test.json"))
	for val in a.keys():
		if len(val) > 2:
			url = a[val]
			folderName = val.replace(" ", "_")
			os.system("mkdir {}".format(folderName))
			for val in range(0, 340, 20):
				tempUrl = url.replace("279.03818", "{}.03818".format(val))
				response = requests.get(tempUrl, stream=True)
				with open('{}/{}.jpg'.format(folderName, val), 'wb') as out_file:
				    shutil.copyfileobj(response.raw, out_file)
				del response

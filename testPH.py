import requests
import json
import random
import threading
import time
import json
import os

COUNT = 0
lock = threading.Lock()
def increment():
	global COUNT
	COUNT = COUNT+1

i = 023524
storeList = []
headers = {
    'pragma': 'no-cache',
    'origin': 'https://www.pizzahut.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    'cache-control': 'no-cache',
    'authority': 'www.pizzahut.com',
    'cookie': '',
    'referer': 'https://www.pizzahut.com/index.php',
}

openNum = "027543"
closedNum = "023524"
fakeNum = "999991"
openStores = []
closedStores = []

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i + n]

def append_record(record, file):
	with open(file, 'a') as f:
		json.dump(record.content, f)
		f.write("\n")

def checkStore(storeNums):
	data = '{"storeNum":"NUM"}'.replace("NUM", str(storeNum))
	# Indicates store number
	response = requests.post('https://www.pizzahut.com/api.php/site/api_ajax/stores/getStoreAjax', headers=headers, data=data)
	if response.json()['response']['phone'] == None:
		print("Not a Real Store")
	elif response.json()['response']['longitude'] == 0:
		print("Closed Store")
	else:
		print("Open Store")
#elif
if __name__ == '__main__':
	for i in range(0,999999):
		storeList.append(str(i).zfill(6))
	random.shuffle(storeList)
	listOfStoreNums = chunks(storeList, int(len(storeList)/10))
	# ^ 50 Threads
	def counting():
		print("Started Counting")
		while True:
			time.sleep(15)
			print("{} TOTAL | {} CLOSED | {} OPEN".format(COUNT, len(closedStores), len(openStores)))
	b = threading.Thread(target=counting)
	b.start()
	threads = [threading.Thread(target=checkStore, args=(ar,)) for ar in listOfStoreNums]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()




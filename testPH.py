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
	'cookie': 'pizzabucket=101%7E6; PHPpoolSSL=!pRI5aogn/D8Q9KHT3j0+tfRMVDb1eKv1zMMMKNM3R4ol5r/bKURq6jD4cLj68Q1oNXto/PLhcYh0ZQ==; AKA_A2=A; QOSESSID=j9hu3denet02ah4oji0ldhqg45; www-siteview=www; gtm-session-start=1529872297020; user_state=%7B%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%7D; akadcgtm=dc1; TS01bded03=01166f2bd0fcba29d9ccf59e8823699dfe2c80b9e1c0fead795a62ccc0e9bfbd1db3b72b1f3d021d9f33bb82576096f7441c8bcda9d806a1e03ebc90a3d8a4b86374de21dc4d07e33a2a0d0c4ded068e58c1fe62d961265ad804de8f8f3493a2c563b8fe7e; TS011d6839=01166f2bd03548e56a1a1663a5babe0d7127108d3a7d34a10c99954e2de475bce03ecb706c9f653bb82f5a5556de6fa7c9783dccdad90369d477a949f26522787ffa492199acb80d05585d29a5290502daca90f974; bm_sv=BF8BD8793C85E9A8DD6C0C08CE8CEB5D~dP7TfnvPClScaNMu9eEV5Kl2BqJev67W2Zg4yUhtcqieB/DhVX+G0l9++y532PSm8Hqsny642mLwyTQGALsAoYs4g6TotaRR1ypHT9Q3cwiHQSNjdn6OKwchQhOdAW/Llf42gqJviCElGodBgrKiTBflLdJPLzY7/kzx2xdK0WQ=;',
}

openNum = "027543"
closedNum = "023524"
fakeNum = "999991"

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i + n]

def append_record(record, file):
	with open(file, 'a') as f:
		json.dump(record.text, f)
		f.write("\n")

def checkStore(storeNums):
	for storeNum in storeNums:
		try:
			res = requests.session()
			res.headers.update(headers)
			#print storeNum
			proxies = {"http": "108.59.14.203:13010", "https":"108.59.14.203:13010"}
			data = '{"storeNum":"NUM"}'.replace("NUM", str(storeNum))
			response = res.post('https://www.pizzahut.com/api.php/site/api_ajax/stores/getStoreAjax', headers=headers, data=data, proxies=proxies)
			#print json.dumps(response.json())
			#print response.json()['response']['phone']
			if response.json()['response']['phone'] == None:
				print("Not real store")
			elif response.json()['response']['longitude'] == 0:
				append_record(response, 'closedStores.json')
			else:
				append_record(response, 'openStores.json')
		except Exception as exp:
			print exp
		lock.acquire
		increment()
		lock.release
#elif
if __name__ == '__main__':
	for i in range(0,999999):
		storeList.append(str(i).zfill(6))
	random.shuffle(storeList)
	listOfStoreNums = chunks(storeList, int(len(storeList)/5))
	# ^ 50 Threads
	def counting():
		print("Started Counting")
		while True:
			time.sleep(60)
			print COUNT
	b = threading.Thread(target=counting)
	b.start()
	threads = [threading.Thread(target=checkStore, args=(ar,)) for ar in listOfStoreNums]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()




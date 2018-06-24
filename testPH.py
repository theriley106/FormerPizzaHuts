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
    'cookie': 'pizzabucket=101%7E6; AKA_A2=A; bm_sz=52F2E2F71EAA64B8AD0E3B5A81C3087B~QAAQ5TLFF2UjVC1kAQAAw6Z+M2doMFxz8Xch6nwEzjYg050tEMPKol42tPAxRT/p9E0Tc6xFyvDaG+AFPEv1cRA7BH5Z0+sBdIkgVjgS5hucaxXwJP8FStFEPjUDngOlBKtV53KOz2dhhUp93M/VAAQ6kVNMPKCWWCrJyUblncGtCgeGvjhK4Op/Fh19Crx3; _abck=FF24379959B08F7BC839BE5896078A7217C532E53F1E0000A7FF2F5B6CC28853~0~XHNVMDobWCMOvqHKb+gI/klCkVCQhTrlqZcJyNc0MiM=~-1~-1; QOSESSID=j9hu3denet02ah4oji0ldhqg45; ak_bmsc=778BD878478EAC9A2B01AF8CFE06F93317C532E53F1E0000A7FF2F5BA922CA79~pl+HyJIFXsYCWrVSHvAbeXSxFEgrbz6iRpIEzF3rjF/OPVFoalzpyCqFTpDhN2mIcLevrzLxCSzZqtJ/XyidvETMITsogp6f76+BAdajsgFFYtvAHQ0WoUlCCYE5PSQTtDXpfa3kaTVBRj10yfOZLPYOkxsA0cu7qVQo4bQNiwK/Nyu8WTGROA3ur8+KZDrm/L/0cUk4WbTKPIgSQx4WaS1j21cOBdH/cjjZzxxjQS9S5xbS/GQbszyWoA0lrrB8UUbaPyGMheH89rd4PWc2mHgA==; _4c_=fVLNbtswDH6VQLtmNvVjS8qt2IBhhx13HmyJgo0lliArc9ci714qSbsCBeaDIZMfvx%2FKz2ybcGEH3glrdKcNGAl79hv%2FruzwzFyq7z%2FXY%2FTIDozbpmsE2zNcqMxS9nQOBGMwKmGcVkaDC4H70YU%2BiN47FD4EqDPfHn59%2F1pJNOmBAKmam7CQwKl%2FzkfqTqWk9dC227Y1aX56GqZzaVw8tfPi8bFJU%2FrUHqMbyhyXtV3juUyf3ZDjcV6GNs3oT3EpLQjdKUmkY47bipmIv0w5nnD3I47zEXc9UDNSTPaw%2BBznGiRjwJyvYPpa51Ijv%2Fdwr9J%2B3jWoWDCfKhUdU90Lr3Eo7s%2F%2F5L3s2eNt87azXFnLafOl0ApMr6A%2BhMjk63YFbJDedJ6rgUvUfQCUCKPtNHfcWOcNKV75pO4V3aKEThBBIr7rPH%2BTM6bXIAWYuxxXb3LV%2FA39D353B%2FajuzCOr%2B7WV%2Fk6QP%2BA7PWHgcvlBQ%3D%3D; www-siteview=www; PHPpoolSSL=!hzdmj5pDsp5vJ8SukmIrYxaCaifTeorPyK3sK+kPeD8dQiWUJkZAhE4/utzzkV072AzbXCbvWsT/g88=; TS0118ed69=01da65bfdd956ce949c74cf2c226ac55ab0eda620f6a1061a6961c84c34b4600509b2557102e350032b5837549dcee1ff3431757d787288b00088d89fef40cbb1879d1cf81; gtm-session-start=1529875781959; _ga=GA1.2.1715202034.1529872301; _gid=GA1.2.1469709314.1529872301; _gat_UA-34361514-2=1; user_state=%7B%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%7D; akadcgtm=dc3; TS01bded03=01da65bfdda21f3dd3887d24dd01a18c7104e193226a1061a6961c84c34b4600509b2557100a7dfd0a39c7431b540118aa6a19bc3015e2989256a3319dcbcd37d69bf57223427c804994bd4da1d64be7e528858a60cbd27179b57d0e0181f31f9a4d06b76e; TS011d6839=01da65bfdd14fc4f09c876f67d70157490f72157ae6a1061a6961c84c34b4600509b255710a5fe4b8a93dc6db2250e9509ab5a383187437e9d929bc40d07e4f1b9ee49298cd846f3d911d3127cc475c6336558af98; bm_sv=BF8BD8793C85E9A8DD6C0C08CE8CEB5D~dP7TfnvPClScaNMu9eEV5Kl2BqJev67W2Zg4yUhtcqieB/DhVX+G0l9++y532PSm8Hqsny642mLwyTQGALsAoYs4g6TotaRR1ypHT9Q3cwiGuK38YZTsEhJXkNJebV8JVDATseJW3yCF8VfVwXx8jY1dMpmYGX1rS2h8Y7NjsMs=',
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
	for storeNum in storeNums:
		try:
			res = requests.session()
			res.headers.update(headers)
			#print storeNum
			proxies = {"http": "108.59.14.203:13010", "https":"108.59.14.203:13010"}
			data = '{"storeNum":"NUM"}'.replace("NUM", str(storeNum))
			response = res.post('https://www.pizzahut.com/api.php/site/api_ajax/stores/getStoreAjax', headers=headers, data=data, proxies=proxies, timeout=10)
			#print json.dumps(response.json())
			#print response.json()['response']['phone']
			if response.json()['response']['phone'] == None:
				pass
			elif response.json()['response']['longitude'] == 0:
				append_record(response, 'closedStores.json')
				closedStores.append(storeNum)
			else:
				openStores.append(storeNum)
				append_record(response, 'openStores.json')
		except Exception as exp:
			print exp
			pass
		lock.acquire
		increment()
		lock.release
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




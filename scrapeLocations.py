import requests
import bs4
import csv
import random
import threading
import RandomHeaders
import json
COUNT = 0
lock = threading.Lock()
def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i + n]
formerPizzaHuts = []

THREADS = 10
with open('locations.csv', 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

ADDRESS_LIST = []
i = 0
for valueList in your_list:
	try:
		ADDRESS_LIST.append(valueList[-1].split("(")[0].strip()[:-1])
		i += 1
	except Exception as exp:
		print exp

ADDRESS_LIST = open('formerLocations.txt').split("\n")

addressList = chunks(ADDRESS_LIST, int(len(ADDRESS_LIST)/THREADS))
information = {}


def grabSite(url):
	for i in range(3):
		try:
			proxy = "108.59.14.203:13010"
			proxies = {"http": proxy, "https": proxy}
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{}.0.2171.95 Safari/537.36'.format(random.randint(1, 99))}
			return requests.get(url, headers=headers, proxies=proxies, timeout=10)
		except Exception as exp:
			print exp
			pass

def increment():
	global COUNT
	COUNT = COUNT+1
	print("{} / {}".format(COUNT, i))

def FormerPizzaHut(page):
	valueBool = True
	# Returns true if it's a former pizza hut
	try:
		if "address" in page.select("h4")[0].getText().lower():
			for val in page.select("h5"):
				print val.getText().lower()
				if "pizza hut" in val.getText().lower():
					return False
			return valueBool
		else:
			return "idk"
	except Exception as exp:
		return "idk"

def processLocations(listOfLocations):
	for address in listOfLocations:
		lock.acquire
		increment()
		lock.release
		try:
			addressVal = address
			address = address.replace(',', "%2C").replace(" ", "+")
			url = "https://www.google.com/search?q=" + address
			res = grabSite(url)
			page = bs4.BeautifulSoup(res.text, 'lxml')
			print page.title.string
			if FormerPizzaHut(page) == True:
				formerPizzaHuts.append(addressVal)
				print("{} Former Pizza Huts Found".format(len(formerPizzaHuts)))
		except Exception as exp:
			print exp

def grabImages(listOfLocations):
	for address in listOfLocations:
		lock.acquire
		increment()
		lock.release
		try:
			addressVal = address
			address = address.replace(',', "%2C").replace(" ", "+")
			url = "https://www.google.com/search?q=" + address
			res = grabSite(url)
			page = bs4.BeautifulSoup(res.text, 'lxml')
			print page.title.string
			tempInfo = grabImage(page)
			print tempInfo
			if tempInfo != None:
				information[address] = tempInfo
		except Exception as exp:
			print exp

def grabImage(page):
	try:
		link = "geo1.ggpht.com" + str(page.partition("geo1.ggpht.com"))[2].partition(')')[0][-1]
		return link
	except:
		return



if __name__ == '__main__':
	threads = [threading.Thread(target=grabImages, args=(ar,)) for ar in addressList]
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
	'''with open ("test.txt","w")as fp:
		for line in formerPizzaHuts:
			fp.write(line+"\n")'''
	with open('test.json', 'w') as outfile:
    	json.dump(information, outfile)





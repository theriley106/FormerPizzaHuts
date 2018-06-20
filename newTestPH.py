import requests
import json
openNum = 027543
closedNum = 023524
fakeNum = 999992


def checkStore(storeNum):
	headers = {
    'origin': 'https://www.pizzahut.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,es-US;q=0.8,es;q=0.6,ru-BY;q=0.4,ru;q=0.2,en;q=0.2',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    'referer': 'https://www.pizzahut.com/index.php',
    'authority': 'www.pizzahut.com',
    'cookie': 'BIGipServerPHPpool=!Go8axSziyDf8fCHT3j0+tfRMVDb1eIQ45NjktfRzJH+TvBzQN0ixcT6pXlyrldprF0VZeCk1fp5TfQ==; bm_sz=3583A0892348F68E50B03661B8AB2C97~QAAQlhiujE/RKPljAQAAcAXUGvzt/c/vlDxfoS4aAqQzh0w9Q1ai7nPreukkQZmo6EeNXcSaqhP8Ojj7q7Yl/LjbIL+HWnLD2IAZEuFdxeaUxD4y7sd4Pg+TJcpCXvftMqihozKmpSDREz3Y4tyXjIGdf1iY8qFgJUyFnA27TPN4X0MYwhW+yxYsl7JeMaB/hQ==; PHPpoolSSL=!z+0VJMkyGalwo+nT3j0+tfRMVDb1eOJH1Qc3JXqSyOWnwPolaJ++LOUtbPhAXTk+glWnZez4uTosOkI=; AKA_A2=A; bm_mi=7DE94107BE96F821252E60904AA6237C~T7LpDUnK+9P27Bb6OzETOT0vYThuIgOF4Plzm/zefj77xpiRZUuyKYt8vH0YM0vqaNH8ZwHABkX6I3Oh6OghRvPFezF86FuHbdG8+PHE/lCMlZh5+3EyfZxOK/vlzQdW4VOmPDWSQtgqNEDI2ICb/3dWDGd0aiZp4P1McqRcJ2RYQGuEoJQ0Im9x6D1MyM0GGhXvMnarmMwueglUrQ4SdPWSaM7U9JweVuibBTkmE0K2rCRuh+QEQg6+AqxZZqaiNJndlL7/VYvLEpdt//pxmQ==; _abck=7773EA0DF0BD2F7EAC8D8B2326DB6E008CAE1896E84100001BAF295BA9D7241F~0~stiSx1v10Ryj/Yxy1nGW55Onp+GnPYU0ekNy6EeSQrI=~-1~-1; ak_bmsc=C921042BF4373C66FE5600DD971E4DDE8CAE1896E84100001CAF295BF547CE01~plzWbMFf3zez1vAZIvLumGh+oDNzwOA0ZeLsqdL1yyS21fdJmFT/4KW1SidqUx1maB6PudVXCYDZ5/UGHh5ET95FgeSDyUE6SfpVrykqPZSYZIWA/yfsB8fcAEXe5JUBsNXBsl/0O9P5HP/vEXoi6Za7xuLr9gU2zwEmztpftiiPz6f+hslseDntZhYBUFuamxZvW14ToczDtbJW5LnRvZ5lq3i/YT2vG4eTsQZNHLAgtdrEbYOKHTbKR5G87Vx4FS+efICk/4eD67AWxjSJvVug==; pizzabucket=101%7E43; QOSESSID=jtdmaqto583o9e2p7n137tlp01; www-siteview=www; TS0118ed69=01166f2bd02fab11f727b9b1fc5d2f319d4b2f66cbfb36665b4800140a12c82ed83b99ef2c70cb7f7ceeaf6fe91484cbd9c9169f616c7df9a873b82abd1f3b8ebaff92c2206da65431a4849f271ed9ce29ec78f9caad91a616ebc384632e9c84024d168c59fc617ef1ab41605faceb32bfddbd37e2; gtm-session-start=1529460437005; user_state=%7B%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%7D; QOitct=0; akadcgtm=dc1; TS01bded03=01166f2bd010be61082cf35b0bd7c256afd049115fbaa63b0b380504a03c8c784f32ca75b255bd4b1e049fbdb67e3daeafe1a88d1c31db9a6f7607461d5e59dfcac939556db11bdce549b8c16e303b003bcae4934192cfcfaf7d8668558714ea282e80b870f4a6f563b7d62849b22e00ffc3214dfc; TS011d6839=01166f2bd015fb101d66a90c85baf98e1a5d7df4a42ee5153142fcc3b8268c876533f6b94e6e8fcf7c35b772977e50d4db17072ee1de8e8594b88d7aedaf6d5ad53f5772fd54d0d8b05617ff5c5479dc3a46b48764; bm_sv=CF8D595BAF33BF2F22A7146403A1CDFB~Zoz3PJ9xT1WnT5PlyR4P0J/HAVOT7MmzcWh8q8yMGATXvv1SgsVrUikRd04ppzlqIwv8QmILq2SXWXSiNnMMB34J3GXVc0oXo3y1kTrN/srVaa2WobdqR6AyUadJ/XqckkMixss/kMl1pCBtG6cIl+XjlLEOn9GThkgQcnt+6kY=; _gat_UA-34361514-2=1; _4c_=hZDLbrMwEIVfpXK3EfgyNja7qr9UVfq3XVdgG4GagGVISRPl3TMmF6VS1bIAM%2BfM%2BTxzIHPre1IyyQ0oCvhhsCIf%2Fmsk5YHYkN6fy3FwnpSEmUxmnKyI77FMQnR4btBGKNPcallD0dS0UYw2xnkPlTDKG29r9L08vb%2F%2BSyFc8MJIwXi2gKUGJVHfxjWq7TSFsczzeZ6z0O33VbudMjts8q53fpeFNjzm68FWUzf0Y065kBywuY7DPPqIAc9tHDb%2BQVGsDjgH%2Bd%2F12x3%2BRN%2F4GBdPgvzEQNfYTWnS%2B%2FKlimu5E7A4%2BbhJADyGtA5zHvLtlymPK7I771uCQhkMx5wJB9cKaHrQETt3WTyh1lEroKJOUNpQ7pSthOYA1htlXSIueaLgAhBgwGBAwLyln91wUHCNsjYXHIMbLt19caP29%2BWaur5ebrzSUwNopbhC4PeG4%2FEE; _ga=GA1.2.1232795312.1529458465; _gid=GA1.2.1971344482.1529458465',
	}
	data = '{"occasion":"C","storenum":"NUM","saKey":""}'.replace("NUM", str(storeNum).zfill(6))

	response = requests.post('https://www.pizzahut.com/api.php/site/api_ajax/confirm_location', headers=headers, data=data)
	#print json.dumps(response.json())

	response = response.json()
	#if str(response['user_state']['StoreNumber']).zfill(6) != str(storeNum).zfill(6):

	if "cc_accepted" in str(response):
		return "Actual Store - Currently in Business"
	elif len(response['store_info'].keys()) > 3:
		return "Out of Service"
	else:
		return "Not real store"

if __name__ == '__main__':
	print checkStore(openNum) + " Expected - Actual store"
	print checkStore(closedNum) + " Expected - Out of service"
	print checkStore(fakeNum) + " Expected - Not real store"
	print checkStore("031174")

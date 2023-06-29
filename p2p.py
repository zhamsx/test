import requests
import json

url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = {
  "fiat": "RUB",
  "page":1,
  "rows":10,
  "transAmount":60000,
  "tradeType":"BUY",
  "asset":"USDT",
  "countries":[],
  "proMerchantAds":False,
  "publisherType":None,
  "payTypes":["RosBankNew"],
}

response = requests.post(url=url, headers=headers, json=params).json()
price = response['data'][0]['adv']['price']
print(price)

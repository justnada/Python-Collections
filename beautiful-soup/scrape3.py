from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text

doc = BeautifulSoup(result, 'lxml')

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs:
    name, price = tr.contents[2:4]
    if name.p != None and price.span != None:
        fixed_name = name.p.string
        fixed_price = price.span.string
        prices[fixed_name] = fixed_price

print(prices)
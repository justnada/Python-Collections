from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas

keyword = input("What product do you want to search for?")

url = f'https://www.newegg.com/p/pl?d={keyword}&N=4131'
page = requests.get(url).text
doc = BeautifulSoup(page, 'lxml')

pagination = doc.find('span', class_='list-tool-pagination-text').strong.text
pages = int(str(pagination).split('/')[1])

items_found = {}

products = []
prices = []
links = []

for page in range(1, pages + 1)[:5]:
    url = f'https://www.newegg.com/p/pl?d={keyword}&N=4131&page={page}'
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'lxml')

    div = doc.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
    items = div.find_all(text=re.compile(keyword, re.IGNORECASE))

    if items != []:
        for item in items:
            parent = item.parent

            if parent.name != 'a':
                continue

            link = parent['href']
            next_parent = item.find_parent(class_='item-container')

            try:
                price = next_parent.find(class_='price-current').find('strong').string
                items_found[item] = {'price': int(price.replace(',', '')), 'link': link}
            except:
                pass

        sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])     # sort items from the cheapest

        for item in sorted_items:
            product = item[0]
            price = '${}'.format(item[1]['price'])
            link = item[1]['price']

            products.append(product)
            prices.append(price)
            links.append(link)

        # with open('reccomended-products.csv', 'w', newline='') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow(['Product', 'Price', 'Link'])
        #
        #     for item in sorted_items:
        #         writer.writerow([item[0], '${}'.format(item[1]['price']), item[1]['link']])

        dataset = {'Product' : products, 'Price' : prices, 'Link' : links}

        reccomend_products = pandas.DataFrame(dataset)

        reccomend_products.to_csv('Reccomended Products For {}.csv'.format(keyword))
    else:
        print('items not found')


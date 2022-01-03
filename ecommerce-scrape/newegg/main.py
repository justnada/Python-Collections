from bs4 import BeautifulSoup
import requests
import csv
import re

keyword = input("What product do you want to search for?")


def scrape():

    url = f'https://www.newegg.com/p/pl?d={keyword}&N=4131'
    page = requests.get(url).text
    doc = BeautifulSoup(page, 'lxml')

    pagination = doc.find('span', class_='list-tool-pagination-text').strong.text
    pages = int(str(pagination).split('/')[1])

    print('We found products in {} pages'.format(pages))

    max_page = int(input('How many pages that want to be search?'))

    items_found = {}

    for page in range(1, pages + 1)[:max_page]:

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

            with open('Reccomended Products For {}.csv'.format(keyword), 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Product', 'Price', 'Link'])

                for item in sorted_items:
                    print('Inserting data to csv files...')
                    writer.writerow([item[0], '${}'.format(item[1]['price']), item[1]['link']])

        else:
            print('items not found')


if __name__ == '__main__':
    scrape()

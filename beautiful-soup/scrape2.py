from bs4 import BeautifulSoup
import requests
import re

with open('html/index2.html', 'r') as f:
    doc = BeautifulSoup(f, 'lxml')

# tags = doc.find("option")
# tags['value'] =  'new value'
# tags['selected'] = 'false'
# tags['color'] = 'blue'

# tags = doc.find_all(['a', 'option', 'p'])

# tags = doc.find_all('option', text='Diploma')

# tags = doc.find_all(class_='btn-item')

# tags = doc.find_all(text=re.compile("\$.* "), limit=1)
#
# for tag in tags:
#     print(tag.strip())

tags = doc.find_all('input', type='text')

for tag in tags:
    tag['placeholder'] = 'i change you'
    print(tag)

with open('html/changed2.html', 'w') as f:
    f.write(str(doc))
    # f.write(doc.prettify())

# print(tags)
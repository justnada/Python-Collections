import os
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions,Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['PATH'] += r'C:\SeleniumDrivers'  # change it to your needs

option = ChromeOptions()
option.add_experimental_option('detach', True)

driver = Chrome(options=option)
# driver.get('https://www.jobstreet.co.id/id/job-search/job-vacancy.php?ojs=1')
driver.get('https://www.jobstreet.co.id/id/job-search/python-jobs/')

# print('Enter keywords for jobs searching')
# keyword = input('>')
# print('Searching jobs {}...\n'.format(keyword))

def find_jobs():

    try:
        # searchInput = driver.find_element(By.ID, 'searchKeywordsField')
        # searchInput.send_keys(keyword)
        # searchInput.send_keys(Keys.RETURN)

        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')

        titles = soup.findAll('span', class_='sx2jih0')
        companies = soup.findAll('span', class_='sx2jih0 zcydq82q _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8')

        i = 0

        for title in titles:
            print('Job title : {}'.format(title.text.strip()))
            print('Company : {}'.format(companies[i].text.strip()))
            i += 1


        # for company in companies:
        #     print('Company : {}'.format(company.text.strip()))

    finally:
        print('Done successfully!')


find_jobs()
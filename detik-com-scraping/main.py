import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from insert_news import insert_news
from fetch_news import fetch_news
import csv

os.environ['PATH'] += r'C:/SeleniumDrivers'

options = ChromeOptions()
options.add_experimental_option('detach', True)

keyword = input('Search something in detik.com : ')

driver = Chrome(options=options)
url = 'https://www.detik.com/'
driver.get(url)

news_found = []
links = []


def scraping():
    wait = WebDriverWait(driver, 10)

    try:
        search_box = wait.until(EC.presence_of_element_located((By.NAME, 'query')))
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

        page = 1

        while page <= 2:

            print(f'Scraping page {page}...\n')

            articles_container = driver.find_element(By.CSS_SELECTOR, "div[class='list media_rows list-berita']")
            articles = articles_container.find_elements(By.TAG_NAME, 'article')

            for article in articles:
                title = wait.until(lambda n: article.find_element(By.TAG_NAME, 'h2'))
                link = wait.until(lambda l: article.find_element(By.CSS_SELECTOR, 'article > a')).get_attribute('href')

                news_found.append(title.text)
                links.append(link)

            page += 1
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, str(page)))).click()
    finally:
        print('\nScraping data succeed!\n')
        driver.quit()


def generate_csv():
    with open(f'csv_results/Detik_com Keyword {keyword}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Keyword', 'Judul', 'Link'])

        print('Generating csv files...\n')
        for i, n in enumerate(news_found):
            writer.writerow([keyword, n, links[i]])


def insert_data():
    for index, news in enumerate(news_found):
        # print(news, links[index])
        insert_news(news, links[index])


if __name__ == '__main__':
    scraping()
    generate_csv()
    insert_data()

    news_data = None

    try:
        news_data = fetch_news()
    finally:
        if news_data is not None:
            for data in news_data:
                print(data)

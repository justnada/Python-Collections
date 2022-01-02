import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas

os.environ['PATH'] += r'C:/SeleniumDrivers'

options = ChromeOptions()
options.add_experimental_option('detach', True)

keyword = input('Ketik berita yang ingin anda cari : ')

driver = Chrome(options=options)
url = 'https://www.detik.com/'
driver.get(url)

wait = WebDriverWait(driver, 10)

news_found = []
links = []

try:
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'query')))
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    page = 1

    while page <= 5:

        print(f'Scraping page {page}...\n')

        articles_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='list media_rows list-berita']")))
        articles = articles_container.find_elements(By.TAG_NAME, 'article')

        for article in articles:
            title = wait.until(lambda n: article.find_element(By.TAG_NAME, 'h2'))
            link = wait.until(lambda l: article.find_element(By.CSS_SELECTOR, 'article > a')).get_attribute('href')

            news_found.append(title.text)
            links.append(link)

        page += 1
        next_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, str(page)))).click()

    news = {'Judul': news_found, 'Link': links}
    csv = pandas.DataFrame(news)
    csv.to_csv(f'Detik_com Keyword {keyword}.csv')

finally:
    print('\nPrograms end')
    driver.quit()
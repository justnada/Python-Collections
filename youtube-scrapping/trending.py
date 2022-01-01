import os
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions, Chrome

def main():
    # set path for chrome driver
    os.environ['PATH'] += r"C:/SeleniumDrivers"

    # set option to keep open chrome driver
    option = ChromeOptions()
    option.add_argument('--headless')
    option.add_experimental_option("detach", True)

    # initialize driver
    driver = Chrome(options=option)

    # get url for chrome driver
    driver.get('https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl')

    # get every content in that page
    content = driver.page_source.encode('utf-8').strip()

    # initialize beautiful soup with lxml converter
    soup = BeautifulSoup(content, 'lxml')

    titles = soup.findAll('a', id='video-title')
    views = soup.findAll('span', class_='style-scope ytd-video-meta-block')
    video_urls = soup.findAll('a', id='video-title', href=True)

    i = 0  # views and time
    j = 0  # urls

    for title in titles[:20]:
        with open('trending-videos/{}.txt'.format(j), 'w', encoding='utf-8') as file:
            file.write('Rank : {} \n'.format(j))
            file.write('Title : {} \n'.format(title.text.strip()))
            file.write('Total Views : {} \n'.format(views[i].text))
            file.write('Upload Time : {} \n'.format(views[i + 1].text))
            file.write('Video URL : https://www.youtube.com{} \n'.format(video_urls[j]['href']))

        # print('\nTitle: {}\nTotal Views: {}\nUpload Time: {}\nLink: https://www.youtube.com{}'.format(title.text.strip(), views[i].text, views[i + 1].text, video_urls[j]['href']))

        i += 2
        j += 1

        print(f'Files saved {j}')

main()
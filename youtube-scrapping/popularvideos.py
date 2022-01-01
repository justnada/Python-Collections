import os
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions, Chrome

urls = [
    'Freecodecamp',
    'amigoscode',
    'ProgrammerZamanNow',
    'TraversyMedia'
]

def main():
    # set path for chrome driver
    os.environ['PATH'] += r"C:/SeleniumDrivers"

    # set option
    option = ChromeOptions()
    option.add_argument('--headless')
    option.add_experimental_option('detach', False)

    # initialize driver
    driver = Chrome(options=option)

    for url in urls:

        # get url for chrome driver
        driver.get('https://www.youtube.com/c/{}/videos?view=0&sort=p&flow=grid'.format(url))

        # get every content in that page
        content = driver.page_source.encode('utf-8').strip()
        # content = requests.get(f'https://www.youtube.com/c/{url}/videos?view=0&sort=p&flow=grid').text

        # initialize beautiful soup with lxml converter
        soup = BeautifulSoup(content, 'lxml')

        titles = soup.findAll('a', id='video-title')
        views = soup.findAll('span', class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a', id='video-title', href=True)

        print('\n{} Channel : https://www.youtube.com/c/{}'.format(url, url))

        i = 0  # views and time
        j = 0  # urls

        for title in titles[:5]:

            with open(f'popular-videos/{url}{j}.txt', 'w') as f:
                f.write(f'Channel {url} : https://www.youtube.com/c/{url} \n')
                f.write(f'Title : {title.text.strip()} \n')
                f.write(f'Ranks : {j+1} from the most popular {url} videos \n')
                f.write(f'Views : {views[i].text} \n')
                f.write(f'Upload Time : {views[i + 1].text} \n')
                f.write(f'Link : https://www.youtube.com{video_urls[j]["href"]}')

            i += 2
            j += 1

            print(f'Files saved {j}')

main()
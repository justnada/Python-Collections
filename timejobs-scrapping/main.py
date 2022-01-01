from bs4 import BeautifulSoup
import requests
import time

print('Search keywords')
keyword = input('>')
print('Searching for {}'.format(keyword))

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={}&txtLocation='.format(keyword)).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        if 'few' in published_date:
            company_name = job.find('h3', 'joblist-comp-name')
            company_name_clear = next(company_name.children).text.strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '').replace(',', ', ')
            more_info = job.find('header').h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'job-posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name : {company_name_clear} \n')
                    f.write(f'Required Skills : {skills.strip()} \n')
                    f.write(f'More Info : {more_info}')
                print(f'Files saved : {index}')

# used to execute some code only if the file was run directly, and not imported
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
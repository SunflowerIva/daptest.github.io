# in this code, I am trying to find job application with the serach of 'python' 
from bs4 import BeautifulSoup
import requests
import time

# here I am trying to find skills that I am not familiar with so that i can rule them out
print('Put some skill that you  not are familiar with')
unfamliar_skill = input('>')
print(f'Filtering out {unfamliar_skill}')

# In this segment, I am looking for jobs on this website 
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")

    for job in jobs:
        posted_date = job.find('span', class_ = 'sim-posted').span.text
# in this portion of the code, I am trying to find job within a few days and not everything so the files i get back aren't too huge
        if 'few' in posted_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','') 
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','') 
            more_info = job.header.h2.a['href']
# And here again I am trying to rule out skills I dont know from the job search           
            if unfamliar_skill not in skills:
                posted_date = job.find('span', class_ = 'sim-posted').span.text

                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}") 

                print('')
# the time i want this  program running 
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
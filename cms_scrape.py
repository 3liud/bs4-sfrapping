# Import libraries
from bs4 import BeautifulSoup
import requests
import csv 

#Url links
links = [
    'https://editorial.rottentomatoes.com/guide/100-best-classic-movies/', 
    'https://editorial.rottentomatoes.com/guide/100-best-classic-movies/2/', 
    'https://editorial.rottentomatoes.com/guide/100-best-classic-movies/3/', 
    'https://editorial.rottentomatoes.com/guide/100-best-classic-movies/4/',
    'https://editorial.rottentomatoes.com/guide/100-best-classic-movies/5/'\
        ]

for lnk in links:
    source = requests.get(lnk).text 
    soup = BeautifulSoup(source, 'lxml')

# create output file
csv_file = open('data/rotten_tomatoes.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['movie_title', 'critic_consensus', 'rt_score', 'prod_year', 'movie_num'])

# loop thro the website and fetch needed data
for entry in soup.find_all('div', class_ = 'row countdown-item'):
    movie_title = entry.h2.a.text
    critic_consensus = entry.find('div', class_='info critics-consensus').text.split(':')[1]
    critic_consensus = critic_consensus.lstrip()
    rt_score = entry.find("span", class_='tMeterScore').text
    prod_year = entry.find('span', class_ ='subtle start-year').text
    movie_num = entry.find('div', class_= 'countdown-index').text
    
    csv_writer.writerow([movie_title, critic_consensus, rt_score, prod_year, movie_num])

# close the file and save
csv_file.close()

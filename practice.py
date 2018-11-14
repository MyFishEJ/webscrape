#!usr/bin/python

import requests 
from bs4 import BeautifulSoup
import csv


#collects and parses first page
url = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm').text
soup = BeautifulSoup(url, 'html.parser')

#removes ugly links at the end of the page so we only have names
last_links = soup.find(class_ = 'AlphaNav')
last_links.decompose()

f = csv.writer(open('practice.csv','w'))
f.writerow(['Name','Link'])

#pulls text from the BodyText div
artist_name_list = soup.find(class_ = 'BodyText')

#pulls text from all instances of <a> within BodyText div
artist_name_list_items = artist_name_list.find_all('a')

#for loop to print out all artists names
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    #uses beautiful soup's get(href) method to get url of page
    links = 'https://web.archive.org' + artist_name.get('href')
    #print(names) if i want to print names directly on commandline
    #print(links) ^ but links

    f.writerow([names, links])






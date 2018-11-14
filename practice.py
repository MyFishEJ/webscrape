#!usr/bin/python

import requests 
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('practice.csv','w'))
f.writerow(['Name','Link'])

#initialize list to hold pages
pages = []

#populating initialized list with following for loop, iterates for 4 pages in the z section
for i in range(1, 5):
    #i is the integer for page number -> converted to a string
    #.htm creates a list of the string in pages list 
    #append adds results to the ends of pages list
    page = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(page)

#for loop that goes through each page
for item in pages:
    #collects and parses from item in pages
    url = requests.get(item)
    soup = BeautifulSoup(url.text, 'html.parser')

    #removes ugly links at the end of the page so we only have names
    last_links = soup.find(class_ = 'AlphaNav') 
    last_links.decompose()

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






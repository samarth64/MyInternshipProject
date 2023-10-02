import requests
from bs4 import BeautifulSoup
import csv

# Making a GET request
r = requests.get('https://mechomotive.com/google-summer-internship-program-2024/')
l=[]
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', id='main')

for link in soup.find_all('a'):
    l.append(link.get('href'))
with open("webscraping.txt","w") as cv:
    writer= csv.writer(cv)
    writer.writerow(l)
    cv.close()
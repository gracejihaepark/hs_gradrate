import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
import json
import config



#get url links for all the districts
dist_url = 'https://data.nysed.gov/profile.php?instid=7889678368'
page = requests.get(dist_url)
soup = BS(page.content, 'html.parser')

#select html with district links
dist_results = soup.select('[href^="profile.php?instid="]')
dist_results


#take links out of html
url_part = [a['href'] for a in dist_results]
# url_part


#append front protion of url to links
dist_urls = []
for url in url_part:
    dist_urls.append('https://data.nysed.gov/' + url)
dist_urls


#function to get urls for all schools in all districts
def get_hs_ids(url):
    page = requests.get(url)
    soup = BS(page.content, 'html.parser')
    hs_results = soup.select('[href^="profile.php?instid="]')
    hs_url_part = [a['href'] for a in hs_results]
    hs_ids = []
    for url in hs_url_part:
        urlpart = url.replace('profile.php?instid=','')
        hs_ids.append(urlpart)
    return hs_ids


#get all school ids
all_hs = []
for url in dist_urls:
    all_hs.extend(get_hs_ids(url))
len(all_hs)

#save school ids in csv file
hs_ids = pd.DataFrame(all_hs)
hs_ids.to_csv("hs_ids.csv")


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = bs(page.text, 'html.parser')

star_table = soup.find('table')
temp_list=[]
table_rows=star_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td') 



import pandas as pd 
import csv
import requests
from bs4 import BeautifulSoup
import time 

bright_stars = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(bright_stars)
soup = BeautifulSoup(page.text, "html.parser")
starstable=soup.find('table')
temp_list=[]
tablerows=starstable.find_all('tr')
for tr in tablerows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names=[]
Star_distance=[]
Star_mass=[]
Star_radius=[]


for i in range (1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Star_distance.append(temp_list[i][3])
    Star_mass.append(temp_list[i][5])
    Star_radius.append(temp_list[i][6])

df= pd.DataFrame(list(zip(Star_names,Star_distance,Star_mass,Star_radius)), columns=['Star Names', 'star distance', 'star mass','star radius'])                                                                                                                                                                                                                                                                                                                                                        
df.to_csv('startdfaidfmlszfsfcdf.csv')                    
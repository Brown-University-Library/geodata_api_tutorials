# -*- coding: utf-8 -*-
"""
Use the Census API to get 2020 census population from
the public redistricting file with loops for multiple geos

https://www.census.gov/data/developers/data-sets/decennial-census.html
https://www.census.gov/library/reference/code-lists/ansi.html
https://mcdc.missouri.edu/applications/geocodes/

Frank Donnelly GIS and Data Librarian
Brown University Library
July 21, 2022
"""
import requests,csv

year='2020'
dsource='dec' # the survey i.e. decennial census, acs, etc
dseries='pl' # a dataset within the survey
cols='NAME,P1_001N' # census variables - total population
outfile='census_pop2020_sne.csv'
keyfile='census_key.txt'

states=['09','25','44'] # list of the states to iterate through

with open(keyfile) as key:
	api_key=key.read().strip()

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dseries}'

county_data=[] # list to hold data we retrieve
for i,v in enumerate(states): # idx number and value, get all counties * for each state
    try:
        data_url = f'{base_url}?get={cols}&for=county:*&in=state:{v}&key={api_key}'
        response=requests.get(data_url)
        popdata=response.json()
    except Exception as e:
        print(e)
        print('Problem at index',i,'value',v)
    if i==0: # if we are on the first record, grab the header row / column names
        for record in popdata:
            county_data.append(record)
    else: # otherwise just take the data, we don't need the header each time
        for record in popdata[1:]:
            county_data.append(record)


for record in county_data:
    print(record)
    
with open(outfile, 'w', newline='') as writefile:
    writer=csv.writer(writefile, quoting=csv.QUOTE_MINIMAL, delimiter=',')
    writer.writerows(popdata)
    
api_key='' 
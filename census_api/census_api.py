# -*- coding: utf-8 -*-
"""
Use the Census API to get 2020 census population from
the public redistricting file

https://www.census.gov/data/developers/data-sets/decennial-census.html
https://www.census.gov/library/reference/code-lists/ansi.html
https://mcdc.missouri.edu/applications/geocodes/

Frank Donnelly GIS and Data Librarian
Brown University Library
Feb 28, 2022 / rev July 21, 2022
"""
import requests,csv

year='2020'
dsource='dec' # the survey i.e. decennial census, acs, etc
dseries='pl' # a dataset within the survey
cols='NAME,P1_001N' # census variables - total population
state='44' # ansi fips codes for states; use asterisk * for all states
place='19180,54640,59000,74300' # ansi fips codes cities / towns; use asterisk * for all places
outfile='census_pop2020.csv'
keyfile='census_key.txt'

with open(keyfile) as key:
	api_key=key.read().strip()

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dseries}'

# for sub-geography within larger geography - geographies must nest
data_url = f'{base_url}?get={cols}&for=place:{place}&in=state:{state}&key={api_key}'

response=requests.get(data_url)

popdata=response.json()
for record in popdata:
    print(record)
    
with open(outfile, 'w', newline='') as writefile:
    writer=csv.writer(writefile, quoting=csv.QUOTE_MINIMAL, delimiter=',')
    writer.writerows(popdata)
    
api_key='' 
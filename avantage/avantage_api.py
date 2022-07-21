# -*- coding: utf-8 -*-
"""
Use Alpha Vantage API to get recent stock data at various intervals
LIMIT 5 API requests per minute / 500 requests per day
Docs: https://www.alphavantage.co/documentation/#intraday

Frank Donnelly GIS and Data Librarian
Brown University Library
Sept 10, 2021 / rev July 21, 2022
"""

import requests,csv
from datetime import date

#Set variables
series='TIME_SERIES_INTRADAY' #Gets last 1 to 2 months of data
ticker='IBM' # Ticker symbol
interval='1min' # 1min, 5min, 15min, 30min
outsize='compact' #compact = first 100 records; change to 'full' to get everything
keyfile='av_key.txt'

base_url = 'https://www.alphavantage.co/query?function='

#Read api key in from file
with open(keyfile) as key:
    api_key=key.read().strip()

#Retrieve data, print output to screen
data_url = f'{base_url}{series}&symbol={ticker}&interval={interval}&outputsize={outsize}&apikey={api_key}'
response=requests.get(data_url)
stockdata=response.json()

tlabel='Time Series ('+interval+')' # Separate data from metadata
trades=stockdata.get(tlabel)

tlist=[]
for k,v in trades.items(): 
    record=[]
    record.append(k) # Top dictionary has date key and sub-dict of values
    for v2 in v.values(): # Subdict has key varnames and value variables
        record.append(v2)
    tlist.append(record)

# Generate header row from the first record of values
header=[]
header.append('date_time')
first_rec = list(trades.values())[0]
for k in first_rec.keys():
    colname=k.split('.')[1].strip()
    header.append(colname)
tlist.insert(0,header)

tcount=len(tlist)-1
        
#Write data to CSV
today=str(date.today())
outfile='av_'+ticker+'_'+today+'.csv'
with open(outfile, 'w', newline='') as writefile:
    writer = csv.writer(writefile, quoting=csv.QUOTE_ALL, delimiter=',')
    writer.writerows(tlist) 

print('Wrote',tcount,'records to file',outfile)

api_key='' 
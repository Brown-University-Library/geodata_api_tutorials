# -*- coding: utf-8 -*-
"""
Use NY Times API Archive API to get articles with specific terms
for single month and year, write to CSV
Docs: https://developer.nytimes.com/docs/archive-product/1/overview

Frank Donnelly GIS and Data Librarian
Brown University Library
April 8, 2022 / rev July 21, 2022
"""

import requests,json,csv

#Set variables
year='2018'
month='10'
keyfile='nyt_key.txt'
dumpfile='news_dump.json'
terms=['election','vote','voting','midterm'] # terms to search for
esearch=['abstract','lead_paragraph'] # what to search through
#Some desired elements from NYT are nested
ekeep=[['headline','main'],
       ['byline','original'],
       'pub_date','abstract','lead_paragraph','word_count',
        'uri','web_url']
outfile='nyt_extract_{}{}.csv'.format(year,month)

base_url = 'https://api.nytimes.com/svc/archive/v1/'

#Read api key in from file
with open(keyfile) as key:
    api_key=key.read().strip()

"""
REQUESTS BLOCK - comment OUT after successful request when
testing and making modifcations to the rest of the script
May take a couple minutes to run...
"""
data_url = f'{base_url}/{year}/{month}.json?&api-key={api_key}'
response=requests.get(data_url)
newsdata=response.json()
with open(dumpfile, 'w') as f:
    json.dump(newsdata, f) 
"""
END REQUESTS BLOCK
"""

#Load saved data to manipulate
with open(dumpfile, 'r') as f:
    newsdata=json.load(f)

news=newsdata['response']['docs'] #flatten results

i=0    
for record in news:
    if any(t in record['abstract'].lower() for t in terms) is True:
        i=i+1        
print('Total number of articles returned:',newsdata['response']['meta']['hits'])
print('Articles returned with term in abstract:',i)

keep_news=[] # main list of articles we want to keep

for record in news:
    elist=[] # list of elements we want to search through
    klist=[] # list of individual article elements we want to keep
    for es in esearch:
        elist.append(record[es])
    for content in elist:
        # As soon as you find any term in an element, capture and break
        if any(t in content.lower() for t in terms) is True:
            for ek in ekeep:
                if type(ek) is list: # handle nested elements
                    klist.append(record[ek[0]][ek[1]])
                else: # handle single elements
                    klist.append(record[ek])
            keep_news.append(klist)
            break        
        else:
            pass

print('Articles returned with term in abstract or lead:',len(keep_news))

header=[]
for ek in ekeep:
    if type(ek) is list:
        header.append(ek[0])
    else:
        header.append(ek)
          
with open(outfile, 'w', newline='') as writefile:
    writer=csv.writer(writefile, quoting=csv.QUOTE_MINIMAL, delimiter=',')
    writer.writerow(header)
    writer.writerows(keep_news)   
    
print('Wrote results to',outfile)

api_key=''    
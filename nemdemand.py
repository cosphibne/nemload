# this program will do the following:
# scrape http://nemweb.com.au/Reports/CURRENT/Operational_Demand/ACTUAL_DAILY/
# put the extracted links into a database
# use the database to track whether a file has been downloaded
# unzip the file to extract the csv
# use the database to track that the csv has been unzipped
# read in the csv data
# store the data in the database

# this program will require the following packages
# urllib, beautifulsoup, sqlite3
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import sqlite3 as db
import ssl


#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://nemweb.com.au/Reports/CURRENT/Operational_Demand/ACTUAL_DAILY/'

#read the website using urllib.request.urlopen(...).read()
html = urllib.request.urlopen(url, context = ctx).read()
#BeautifulSoup it
soup = bs(html,'html.parser')

# extract all the anchor <a> tags
# find_all(name, attrs, recursive, string, limit, **kwargs)

tags = soup.find_all('a')
tagslist = list()
print(type(tags))
# we now have abs.'ResultSet' of all the tags
for tag in tags:
    #print(tag.get('href', None))
    tagslist.append(tag.get('href', None))
#now we have a python list of strings
print(type(tagslist), len(tagslist))
print(tagslist[0],%n, tagslist[1])

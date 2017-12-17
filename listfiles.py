import urllib.request, urllib.parse, urllib.error
import sqlite3 as db
import ssl
from os import listdir
from os.path import isfile, join

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

homepage = 'http://nemweb.com.au'
dataloc = 'd:\pyth\data\\'

conn = db.connect('nem_daily_load_files.sqlite')
cur = conn.cursor()

#how many files to download?
cur.execute(''' SELECT COUNT(filename) FROM filelist
                WHERE download = ? AND
                url LIKE '%zip' ''', (0,))
number_of_files = cur.fetchone()[0]
print(number_of_files)

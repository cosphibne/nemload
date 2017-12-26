#this is the program that will download the files from the website
#once downloaded, it checks if the file on the harddrive has the same name as
#the file in the html.
#if so, it updates the database to indicate teh file has been downloaded

import urllib.request, urllib.parse, urllib.error
import sqlite3 as db
import ssl
from os import listdir
from os.path import isfile, join
import time

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

homepage = 'http://nemweb.com.au'
dataloc = 'd:\pyth\data\\'

conn = db.connect('nem_daily_load_files.sqlite')
cur = conn.cursor()

#check existing files have been logged in database
existingfiles = [f for f in listdir(dataloc) if isfile(join(dataloc,f))]
for fid in existingfiles:
    cur.execute(''' UPDATE filelist SET
                download = 1 WHERE
                filename = ? ''', (fid,))
conn.commit()

#how many files to left download?
cur.execute(''' SELECT COUNT(filename) FROM filelist
                WHERE download = ? AND
                url LIKE '%zip' ''', (0,))

number_of_files = cur.fetchone()[0]

while number_of_files > 0:

    cur.execute(''' SELECT COUNT(filename) FROM filelist
                    WHERE download = ? AND
                    url LIKE '%zip' ''', (0,))
    number_of_files = cur.fetchone()[0]
    if number_of_files == 0: break

    cur.execute(''' SELECT id FROM filelist WHERE
                    download = ? AND
                    url LIKE '%zip' ''', (0,))
    file_id = cur.fetchone()[0]

    cur.execute(''' SELECT url FROM filelist WHERE
                    id = ? ''', (file_id,))

    fileloc = homepage + cur.fetchone()[0]

    cur.execute(''' SELECT filename FROM filelist WHERE
                    id = ? ''', (file_id,))
    filename = cur.fetchone()[0]
    fullfilename = dataloc + filename

    print('There are ',number_of_files,' to go')
    print('About to download: ', fileloc)
    print('and save it to: ', dataloc)
    print('with filename', filename)
    print('but first I''ll pause to allow for an interrupt')

    time.sleep(5)
    print('ok, downloading...')

#download the file
    urllib.request.urlretrieve(fileloc, fullfilename)

    onlyfiles = [f for f in listdir(dataloc) if isfile(join(dataloc,f))]
    for fid in onlyfiles:
        cur.execute(''' UPDATE filelist SET
                    download = 1 WHERE
                    filename = ? ''', (fid,))

    conn.commit()

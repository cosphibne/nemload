#this is the program that will extract the files that have been downloaded
#once unzipped, it updates the database to indicate the file has been extracted

import zipfile
import sqlite3 as db
from os import listdir
from os.path import isfile, join
ikmport re


dataloc = 'd:\pyth\datatest\\'

conn = db.connect('nem_daily_load_files.sqlite')
cur = conn.cursor()

#how many files left to unzip?
cur.execute(''' SELECT COUNT(filename) FROM filelist
                WHERE unzipped = ? AND
                filename LIKE '%zip' ''', (0,))

number_of_files = cur.fetchone()[0]
print(number_of_files)

cur.execute(''' SELECT filename FROM filelist
                WHERE unzipped = ? AND
                filename LIKE '%zip' ''', (0,))

#filelist = cur.fetchall()
# get a filename from the query
for f in range(number_of_files):
    filename = cur.fetchone()[0]
    #print(dataloc + filename)
#unzips the file
    zip_ref = zipfile.ZipFile(dataloc + filename, 'r')
    zip_ref.extractall(dataloc)
    zip_ref.close()

#check that the file has been unzipped
#read the list of files in the directory
#if a file with a matching name existing with .csv then mark as successfully unzipped

onlyfiles = [f for f in listdir(dataloc) if isfile(join(dataloc, f))]
print(onlyfiles)
##this isn't done yet
for f in onlyfiles:
    print(f)
    csv = (re.findall('/([A-Z0-9_]*?.csv)',f))
    if len(fn) == 0:
        fn = ("None")
    print(fn)

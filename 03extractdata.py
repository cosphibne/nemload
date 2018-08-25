#this is the program that will extract the files that have been downloaded
#once unzipped, it updates the database to indicate the file has been extracted

import zipfile
import sqlite3 as db
from os import listdir, remove
from os.path import isfile, join
import re



dataloc = 'd:\pyth\data\\'

conn = db.connect('nem_daily_load_files.sqlite')
cur = conn.cursor()

#how many files left to unzip?
cur.execute(''' SELECT COUNT(filename) FROM filelist
                WHERE unzipped = ? AND download = ? AND
                filename LIKE '%zip' ''', (0,1,))

number_of_files = cur.fetchone()[0]
print(number_of_files)
input('Press Enter to continue')

cur.execute(''' SELECT filename FROM filelist
                WHERE unzipped = ? AND
                filename LIKE '%zip' ''', (0,))

#filelist = cur.fetchall()
#%%
# get a filename from the query
for f in range(number_of_files):
    filename = cur.fetchone()[0]
    print(dataloc + filename)

#unzips the file
    try:
        zip_ref = zipfile.ZipFile(dataloc + filename, 'r')
        print(filename, ' opened')
        zip_ref.extractall(dataloc)
        zip_ref.close()
        #remove(dataloc+f) #this deletes a file
        
    except:
        continue
#%%

#check that the file has been unzipped
#read the list of files in the directory
#if a file with a matching name existing with .csv then mark as successfully unzipped

onlyfiles = [f for f in listdir(dataloc) if isfile(join(dataloc, f))]
#print(onlyfiles)
##remove the zip files
for f in onlyfiles:
    #print(f)
    csv = (re.findall('([A-Z0-9_]*?.CSV)',f))
    if len(csv) == 0:
        remove(dataloc+f) #this deletes a file
        #csv = ("None, non-CSV file deleted")
#%%

onlycsvfiles = [csvf for csvf in listdir(dataloc) if isfile(join(dataloc, csvf))]

for df in onlycsvfiles:
    fileid = (re.findall('([A-Z0-9_]*?).CSV',df))
    print('fileid =  ', fileid)

    lookupdf = ' '.join(fileid) +'.zip' #creates the zip filename from the csv name
    print('Lookup values = ', lookupdf)
    #looks up the correct record
    cur.execute(''' SELECT id FROM filelist
                    WHERE unzipped = ? AND
                    filename = ? ''', (0, lookupdf))
    try:
        targetfile = cur.fetchone()[0]
        #updates the record to show the file is unzipped
        cur.execute('''UPDATE filelist SET unzipped = ?
                        WHERE id = ?''', (1,targetfile))
    except:
        continue


conn.commit()

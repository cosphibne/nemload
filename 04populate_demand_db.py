# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:07:03 2018

@author: CosPhi
"""

#file needs to read csv files, extract data to an SQL database
# table = pool name
# date field
#time field
#or datetime field
#demand field


import sqlite3 as db
from os import listdir, remove
from os.path import isfile, join
import re
import pandas as pd



dataloc = 'd:\pyth\data\\'

#conn = db.connect('nem_daily_demand.sqlite')
#cur = conn.cursor()

#need to convert (D)D/MM/YYY HH:MM time format to YYYY-MM-DD HH:MM
# in order to import into SQL using datetime(timestring)

filelist = listdir(dataloc) #gets a list of files

filename = filelist[0]
try:
    df = pd.read_csv(join(dataloc, filename), skiprows = 1)
except:
    continue

df['INTERVAL_DATETIME'] = pd.to_datetime(df['INTERVAL_DATETIME'])



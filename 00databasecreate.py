# this program creates two databases
# one is called nem_daily_demand, which stores the database
# the other is called nem_daily_load_files and
# holds a list of files that have been downloaded and unzipped

import sqlite3

conn = sqlite3.connect('nem_daily_load_files_test.sqlite')
cur = conn.cursor()

#creates the first database
cur.executescript('''
DROP TABLE if EXISTS filelist;

CREATE TABLE filelist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    url TEXT NOT NULL UNIQUE,
    filename    TEXT NOT NULL UNIQUE,
    download    INTEGER,
    unzipped    INTEGER,
    createtime	TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

conn.close()

#create the database of daily demand values
conn = sqlite3.connect('nem_daily_demand.sqlite')
cur = conn.cursor()

#creates the first database
cur.executescript('''

DROP TABLE if EXISTS nem_daily_demand;

CREATE TABLE nem_daily_demand (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    datestamp   TEXT NOT NULL UNIQUE,
    state       TEXT NOT NULL UNIQUE,
    demand      REAL not null
    );
    ''')

conn.close()

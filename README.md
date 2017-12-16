# nemload
collection, cleaning and displaying of NEM data. Work for the Coursera specialization course "Capstone: Retrieving, Processing, and Visualizing Data with Python"


This repository will be in Python 3. 

This project will download actual daily demand for each trading interval of the previous day from the AEMO website, and store the received values in a database.  

The general intended process is:

Get DATA
 scrape http://nemweb.com.au/Reports/CURRENT/Operational_Demand/ACTUAL_DAILY/ to identify new filenames

download new files
 
 unzip files
 
 read csv data into a database
 
 delete csv and zip file
 

Present DATA

extract data into python data structure for presentation in a graph

import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import time

edlist = [ ]
for i in range(1,85):
	s = str(i)+".csv"
	print (s)
	with open(s, encoding="utf8", newline='') as f:
	    g = csv.reader(f)
	    for row in g:
	    	edlist.append(row)
	time.sleep(3)
	
print (len(edlist))

#Export CSV
with open("edulist.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = '~')
    
    for val in edlist:
    	writer.writerow(val)


from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import urllib.parse
import re
import csv
import time

'''
THIS FILE EXTRACTS EMAIL IDS FROM THE LIST

'''
linkList = ['http://www.vvc.edu/academic/athletics/athletics-staff.shtml','http://www.wusports.com/staff.aspx','http://athletics.wallacestate.edu/directory/']
mainList =[ ]
for url in linkList:
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
	html = opener.open(url)
	bsObj = BeautifulSoup(html.read(), "html5lib")
	urlBody  = bsObj.body
	rText = str(urlBody)

	initialList = [ ]
	distinctList= [ ]
	

	eRegex = re.compile(r'[a-zA-Z._0-9]+@\w+\.[a-zA-Z._0-9]+')
	resultAll = eRegex.findall(rText) 
	for resultOne in resultAll:
		initialList.append(resultOne)
	for initialResult in initialList:
		if initialResult in distinctList:
			pass
		else:
			distinctList.append(initialResult)
	print(len(distinctList))

	for ab in distinctList:
		colResults = dict([('College Name',url),('Email',ab)])
		mainList.append(colResults)
	



with open('i.csv', 'w', encoding='utf-8', newline = '') as csvfile: #change here
    fieldnames = ['College Name', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()
    for val in mainList:
    	writer.writerow(val)
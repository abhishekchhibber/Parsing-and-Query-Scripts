
from bs4 import BeautifulSoup
import urllib.request 
from urllib.request import urlopen
import re
import time
import csv

schList = [ ]

with open('schoollist.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        schList.append(row[0])


# print (schList [0:3])

gList = [ ]

def staffDir(urlToOpen):

	url = (urlToOpen)
	# print (url)
	opener = urllib.request.build_opener()
	#opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
	opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
	
	try:


		html = opener.open(url)
		bsObj = BeautifulSoup(html.read(), "html5lib")
		urlBody  = bsObj.body

		ranList = [ ]

		ranList.append(url)


		# links = urlBody.a

		links  = urlBody.findAll("a")

		for link in links:

			linkText = link.text
			linkHref = link

			matchA = "Staff"
			matchB = "staff"
			matchC = "directory"
			matchD = "Directory"


			if matchA in linkText or matchB in linkText or matchC in linkText or matchD in linkText:
				su = link['href']
				ranList.append(su)
				# print (su)

	except:
		pass

	print (ranList)

	gList.append(ranList)


	return 


smallListItems = schList

for smallListItem in smallListItems:

	try:
		staffDir(smallListItem)
		time.sleep(5)
		
	except :
		print ("URL unavailable")
		pass
	





# for r in gList:
# 	print (r)

print(len(gList))


#Export CSV
with open("resultss.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = '#')
    
    for val in gList:
    	writer.writerow(val)

try:
	pass
except Exception as e:
	raise e
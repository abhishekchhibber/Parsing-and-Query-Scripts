from selenium import webdriver
import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re






domain = "tripadvisor.com"
query = "best hotel prices"
queryTwo = query.replace(" ","%20")
queryThree = "https://www.google.com/search?q="+queryTwo
# print (queryThree)
print ("Your Query: " + query )

print ("Your Domain: "+ domain)
#driver = webdriver.Firefox()
#driver.get(queryThree)

#get and read the URL
url = (queryThree)
opener = urllib.request.build_opener()
#opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
html = opener.open(url)
bsObj = BeautifulSoup(html.read(), "html5lib")
print ("Searching Page: 1")
items  = bsObj.findAll("div",{"class":"f kv _SWb"})
for item in items:
	itemTxt = item.text
	itemTxtClean = itemTxt.replace("CachedSimilar","")
	if domain in itemTxtClean:
		print("Link to your site: "+itemTxtClean)
	else:
		pass




# checking subsequent pages

footItems = bsObj.findAll("a",{"class":"fl"})
# print (len(footItems))

footList = [ ]
for footer in footItems:
	footLink = footer['href']
	if "&start=" in footLink:
		footlink2 = "https://www.google.com"+footLink
		footList.append(footlink2)

footlength = len(footList)

footnum = 2
for footsoo in footList:
	print ("Searching Page :"+str(footnum))
	futURL = (footsoo)
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
	futhtml = opener.open(futURL)
	futbsObj = BeautifulSoup(futhtml.read(), "html5lib")

	futitems  = futbsObj.findAll("div",{"class":"f kv _SWb"})
	for futitem in futitems:
		futitemTxt = futitem.text
		futitemTxtClean = futitemTxt.replace("CachedSimilar","")
		if domain in futitemTxtClean:
			print("Link to your site: "+futitemTxtClean)
		else:
			pass




	# print (footsoo)
	footnum = footnum+1
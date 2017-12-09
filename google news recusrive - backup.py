import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#get and read the URL
url = ("https://www.google.co.in/search?q=banking&num=100&espv=2&biw=1366&bih=653&tbs=cdr:1,cd_min:01/04/2016,cd_max:15/04/2016,sbd:1&tbm=nws&source=lnt&sa=X&ved=0ahUKEwjp2ICE15DMAhVBJ5QKHWoXDSkQpwUIFA&dpr=1")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
html = opener.open(url)
bsObj = BeautifulSoup(html.read(), "html5lib")
# function to extract links from a given page
def linkExtrator(pageLink):
	''' extracts all the links from the given page '''
	
	itmes  = bsObj.findAll("h3")
	for item in itmes:
		itemA = item.a
		#print(itemA)
		theHeading = itemA.text
		cLinko = itemA['href'] 
		cLinktwo = cLinko.replace("/url?q=","")
		cLinkthree = cLinktwo.replace("&sa=","#")
		cLinkf = cLinkthree.split("#")
		theLink = cLinkf[0]
		print (theHeading,":", theLink)
	return
linkExtrator(url)


#function to extract links from other pages

def recLinkExtrator(pageLink):
	''' extracts all the links from the given page found through recursive links '''
	recursiveUrl = (pageLink)
	recursiveOpener = urllib.request.build_opener()
	recursiveOpener.addheaders = [('User-agent', 'Mozilla/5.0')]
	recusrsiveHTML = recursiveOpener.open(recursiveUrl)
	recursiveBSObj = BeautifulSoup(recusrsiveHTML.read(), "html5lib")
	
	ritmes  = recursiveBSObj.findAll("h3")
	for ritem in ritmes:
		ritemA = ritem.a
		#print(itemA)
		theHeading = ritemA.text
		cLinko = ritemA['href'] 
		cLinktwo = cLinko.replace("/url?q=","")
		cLinkthree = cLinktwo.replace("&sa=","#")
		cLinkf = cLinkthree.split("#")
		theLink = cLinkf[0]
		print (theHeading,":", theLink)
	return
#recLinkExtrator(url)



#pagination for recusrsive scrolling
counter = 1
footItems = bsObj.findAll("a",{"class":"fl"})
for footItem in footItems:
	footItemLink = footItem['href']
	fullfootItem = "https://www.google.co.in"+footItemLink
	try:
		#print("Reading Page no.: ",counter," = ",fullfootItem)
		recLinkExtrator(fullfootItem)
		counter = counter+1
		
	except :
		pass

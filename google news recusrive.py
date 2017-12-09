import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import nltk
from nltk.tag import pos_tag

#get and read the URL
url = ("https://www.google.com/search?q=banking&num=100&espv=2&biw=1366&bih=653&tbs=qdr:y,sbd:1&tbm=nws&source=lnt&sa=X&ved=0ahUKEwjcueHNvPTMAhWJuY8KHQpfCnEQpwUIFQ&dpr=1")
opener = urllib.request.build_opener()
#opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
html = opener.open(url)
bsObj = BeautifulSoup(html.read(), "html5lib")


# function to extract links from a given page
def linkExtrator():
	#extracts all the links from the given page 
	itmes  = bsObj.findAll("h3",{"class":"r _U6c"})
	global listOne # this is a global list
	listOne = [ ] #this creates a list of results of the first page. Is global
	for item in itmes:
		itemA = item.a
		#print(itemA)
		theHeading = itemA.text
		cLinko = itemA['href'] 
		cLinktwo = cLinko.replace("/url?q=","")
		cLinkthree = cLinktwo.replace("&sa=","#")
		cLinkf = cLinkthree.split("#")
		theLink = cLinkf[0]
		#print (theHeading)
		stuff = [theHeading,theLink]
		listOne.append(stuff)
		#print(listOne)
	return listOne

linkExtrator()
#print (len(listOne)) # will show the number of links fetched
#print (listOne[2]) # to check for a specific heading from the list
#linkExtrator(url)



#pagination for recusrsive scrolling

footItems = bsObj.findAll("a",{"class":"fl"})
print (len(footItems))
listTwo = [ ]
for footItem in footItems:
	footItemLink = footItem['href']
	print("trying"+footItemLink)
	fullfootItem = "https://www.google.co.in"+footItemLink
	try:
		recursiveUrl = (fullfootItem)
		recursiveOpener = urllib.request.build_opener()
		recursiveOpener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
		recusrsiveHTML = recursiveOpener.open(recursiveUrl)
		recursiveBSObj = BeautifulSoup(recusrsiveHTML.read(), "html5lib")		
		ritmes  = recursiveBSObj.findAll("h3",{"class":"r _U6c"})
		#listTwo = [ ] #this creates a list of results of the first page. Is global

		for ritem in ritmes:
			ritemA = ritem.a
			#print(itemA)
			theHeading = ritemA.text
			cLinko = ritemA['href'] 
			cLinktwo = cLinko.replace("/url?q=","")
			cLinkthree = cLinktwo.replace("&sa=","#")
			cLinkf = cLinkthree.split("#")
			theLink = cLinkf[0]
			#print (theHeading)
			stuffTwo = [theHeading,theLink]
			listTwo.append(stuffTwo)
			#print(listTwo)
			#print (len(listTwo))
	

	except :
		pass

finalList = listOne+listTwo
#print(len(listTwo))
print("final list: ",len(finalList))

'''
#exporting as a csv
with open("testOne.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = ',')
    
    for val in listOne:
    	writer.writerow([val])
'''

collabList = [ ]
expanList = [ ]
fintecList = [ ]
investList = [ ]
islambkList = [ ]
onlinebkList = [ ]
regulatList = [ ]

for row in finalList:
	rowTitle = row[0]
	
	if "tie-up" in rowTitle or "partner" in rowTitle or "collaborate" in rowTitle or "collaboration" in rowTitle or "partners" in rowTitle or "ties-up" in rowTitle or "mou" in rowTitle or "merge" in rowTitle or "ties up" in rowTitle:			
		collabList.append(row)
	if "IPO" in rowTitle or "rebrand" in rowTitle or "opens" in rowTitle or "expand" in rowTitle or "open" in rowTitle or "grow" in rowTitle or "launch" in rowTitle or "to open" in rowTitle or "expansion" in rowTitle:
		expanList.append(row)
	if  "fintech" in rowTitle or "smartphone" in rowTitle or "tablet" in rowTitle or "online" in rowTitle or "payment bank" in rowTitle or "payments bank" in rowTitle or "bitcoin" in rowTitle or "app" in rowTitle:
		fintecList.append(row)
	if "raise" in rowTitle or "stake" in rowTitle or "funding" in rowTitle or "sells" in rowTitle or "acquire" in rowTitle or "invest" in rowTitle or "raise" in rowTitle or "sell" in rowTitle or "raising" in rowTitle or "merge" in rowTitle:
		investList.append(row)
	if 	"islamic bank" in rowTitle or "islamic banking" in rowTitle or "sharia" in rowTitle or "shariah" in rowTitle or "shariat" in rowTitle:
		islambkList.append(row)
	if "online banking" in rowTitle or "digital" in rowTitle or "m commerce" in rowTitle or "m-commerce" in rowTitle or "fintech" in rowTitle or "online" in rowTitle or "internet" in rowTitle or "mobile banking" in rowTitle or "mobile" in rowTitle:
		onlinebkList.append(row)
	if "RBI" in rowTitle or "probe" in rowTitle or "sebi" in rowTitle or "rule" in rowTitle or "licence" in rowTitle or "permit" in rowTitle or "basel" in rowTitle or "governance" in rowTitle or "IMF" in rowTitle or "bailout" in rowTitle or "regulator" in rowTitle or "government" in rowTitle or "federal" in rowTitle or "federal reserve" in rowTitle or "privatisation" in rowTitle or "privatization" in rowTitle or "bank of England" in rowTitle or "central bank" in rowTitle or "law" in rowTitle or "regualtion" in rowTitle:
		regulatList.append(row)



	else:
		pass

print("Collaboration: ",len(collabList))
print("expansion: ",len(expanList))
print("fintech: ",len(fintecList))
print("investment: ",len(investList))
print("islamic banking: ",len(islambkList))
print("online banking: ", len(onlinebkList))
print("regualtions: ", len(regulatList))

sumIndexed  = len(collabList)+len(expanList)+len(fintecList)+len(investList)+len(islambkList)+len(onlinebkList)+len(regulatList)

print("Total Indexed: ",sumIndexed)
'''
#exporting as a csv
with open("amit.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = ',')
    
    for val in regulatList:
    	writer.writerow([val[0],val[1],"regualtions"])

'''
import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import nltk
from nltk.tag import pos_tag

'''
***THINGS TO DO***
Search all results - first page
Get title, date, company, and Geography
Search title for keywords and sort in lists
Recursive crawling
Export CSV
'''

collabList = [ ]
expanList = [ ]
fintecList = [ ]
investList = [ ]
islambkList = [ ]
onlinebkList = [ ]
regulatList = [ ]


#Get title, date, company, and Geography - Functions + #Search title for keywords and sort in lists

def attributes (bsObj):
	items  = bsObj.findAll("div",{"class":"_cnc"})

	for item in items:

		newsTitle = item.h3.text
		# print(newsTitle)
		newsLink = item.a['href']
		# print(newsLink)
		newsDate = item("span",{"class":"f nsa _uQb"})[0]
		# print(newsDate.text)
		newsSource = item("span",{"class":"_tQb _IId"})[0]
		# print(newsSource.text)
		tokens = nltk.word_tokenize(newsTitle)
		posTags = nltk.pos_tag(tokens)
		pT = [ ]
		for posTag in posTags:
			#print(posTag)
			if posTag[1] == 'NNP':
				pT.append(posTag[0])

		newsComp = " ".join(str(x) for x in pT)
		# print (newsComp)

		selectedStuff = [newsTitle,newsLink,newsDate,newsSource,newsComp]

		rowTitle= newsTitle
		if "tie-up" in rowTitle or "partner" in rowTitle or "collaborate" in rowTitle or "collaboration" in rowTitle or "partners" in rowTitle or "ties-up" in rowTitle or "mou" in rowTitle or "merge" in rowTitle or "ties up" in rowTitle:			
			collabList.append(selectedStuff)
		if "IPO" in rowTitle or "rebrand" in rowTitle or "opens" in rowTitle or "expand" in rowTitle or "open" in rowTitle or "grow" in rowTitle or "launch" in rowTitle or "to open" in rowTitle or "expansion" in rowTitle:
			expanList.append(selectedStuff)
		if  "fintech" in rowTitle or "smartphone" in rowTitle or "tablet" in rowTitle or "online" in rowTitle or "payment bank" in rowTitle or "payments bank" in rowTitle or "bitcoin" in rowTitle or "app" in rowTitle:
			fintecList.append(selectedStuff)
		if "raise" in rowTitle or "stake" in rowTitle or "funding" in rowTitle or "sells" in rowTitle or "acquire" in rowTitle or "invest" in rowTitle or "raise" in rowTitle or "sell" in rowTitle or "raising" in rowTitle or "merge" in rowTitle:
			investList.append(selectedStuff)
		if 	"islamic bank" in rowTitle or "islamic banking" in rowTitle or "sharia" in rowTitle or "shariah" in rowTitle or "shariat" in rowTitle:
			islambkList.append(selectedStuff)
		if "online banking" in rowTitle or "digital" in rowTitle or "m commerce" in rowTitle or "m-commerce" in rowTitle or "fintech" in rowTitle or "online" in rowTitle or "internet" in rowTitle or "mobile banking" in rowTitle or "mobile" in rowTitle:
			onlinebkList.append(selectedStuff)
		if "RBI" in rowTitle or "probe" in rowTitle or "sebi" in rowTitle or "rule" in rowTitle or "licence" in rowTitle or "permit" in rowTitle or "basel" in rowTitle or "governance" in rowTitle or "IMF" in rowTitle or "bailout" in rowTitle or "regulator" in rowTitle or "government" in rowTitle or "federal" in rowTitle or "federal reserve" in rowTitle or "privatisation" in rowTitle or "privatization" in rowTitle or "bank of England" in rowTitle or "central bank" in rowTitle or "law" in rowTitle or "regualtion" in rowTitle:
			regulatList.append(selectedStuff)

		else:
			pass

	return (newsTitle, newsComp, newsSource, newsDate, newsLink)




'''
Setting URL
URl is being set in normal firfox.... after signing in... and setting search ressults to 10

'''
url = ("https://www.google.com/search?q=banking&safe=off&client=firefox-b&biw=1366&bih=420&tbs=sbd:1,qdr:h&tbm=nws&source=lnt&sa=X&ved=0ahUKEwiktO2a3PrMAhULS48KHULzABgQpwUIFQ&dpr=1")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
html = opener.open(url)
bsObj = BeautifulSoup(html.read(), "html5lib")






#Search all results - first page
print ("first page")
attributes (bsObj)

#Recursive crawling

i = 10
for i in range(10,1200,10):
	newlink  = "https://www.google.com/search?q=banking&safe=off&client=firefox-b&biw=1366&bih=645&tbs=qdr:y,sbd:1&tbm=nws&ei=O0xHV-TaH8jwvAT456zADg&start="+str(i)+"&sa=N&dpr=1"
	try:
		print (i)
		recursiveUrl = (newlink)
		recursiveOpener = urllib.request.build_opener()
		recursiveOpener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
		recusrsiveHTML = recursiveOpener.open(recursiveUrl)
		bsObj = BeautifulSoup(recusrsiveHTML.read(), "html5lib")	
		attributes (bsObj)	
		

	

	except :
		pass





	i = i+10










print("Collaboration: ",len(collabList))
print("expansion: ",len(expanList))
print("fintech: ",len(fintecList))
print("investment: ",len(investList))
print("islamic banking: ",len(islambkList))
print("online banking: ", len(onlinebkList))
print("regualtions: ", len(regulatList))

sumIndexed  = len(collabList)+len(expanList)+len(fintecList)+len(investList)+len(islambkList)+len(onlinebkList)+len(regulatList)

print("Total Indexed: ",sumIndexed)




#Export CSV

with open("june1.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = ',')
    
    for val in regulatList:
    	writer.writerow([val,"Regualtions"])
    for val in collabList:
    	writer.writerow([val,"Collaboration"])
    for val in expanList:
    	writer.writerow([val,"Expansion"])
    for val in fintecList:
    	writer.writerow([val,"Fintech"])
    for val in investList:
    	writer.writerow([val,"Investment"])
    for val in islambkList:
    	writer.writerow([val,"Islamic Banking"])
    for val in onlinebkList:
    	writer.writerow([val,"Online Banking"])

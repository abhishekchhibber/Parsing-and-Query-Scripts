import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import nltk
from nltk.tag import pos_tag
import time


with open('banking.csv', encoding="utf8", newline='') as f:
    g = csv.reader(f)
    rowNum = 1
    for row in g:
    	rowNum = rowNum+1
print("Total in CSV: "+str(rowNum))

collabList = [ ]
expanList = [ ]
fintecList = [ ]
investList = [ ]
islambkList = [ ]
onlinebkList = [ ]
regulatList = [ ]

initialList  = [ ]
with open('banking.csv', encoding="utf8", newline='') as red:
    reader = csv.reader(red)
    for iniRow in reader:
    	initialList.append(iniRow)

for row in initialList:
	rowTitle = row[0]
	if "tie-up" in rowTitle or "partner" in rowTitle or "collaborate" in rowTitle or "collaboration" in rowTitle or "partners" in rowTitle or "ties-up" in rowTitle or "mou" in rowTitle or "merge" in rowTitle or "ties up" in rowTitle:
		collabList.append(row)

for row in initialList:
	rowTitle = row[0]
	if "IPO" in rowTitle or "rebrand" in rowTitle or "opens" in rowTitle or "expand" in rowTitle or "open" in rowTitle or "grow" in rowTitle or "launch" in rowTitle or "to open" in rowTitle or "expansion" in rowTitle:
		expanList.append(row)

for row in initialList:
	rowTitle = row[0]
	if  "fintech" in rowTitle or "smartphone" in rowTitle or "tablet" in rowTitle or "online" in rowTitle or "payment bank" in rowTitle or "payments bank" in rowTitle or "bitcoin" in rowTitle or "app" in rowTitle:
		fintecList.append(row)

for row in initialList:
	rowTitle = row[0]
	if "raise" in rowTitle or "stake" in rowTitle or "funding" in rowTitle or "sells" in rowTitle or "acquire" in rowTitle or "invest" in rowTitle or "raise" in rowTitle or "sell" in rowTitle or "raising" in rowTitle or "merge" in rowTitle:
		investList.append(row)


for row in initialList:
	rowTitle = row[0]
	if 	"islamic bank" in rowTitle or "islamic banking" in rowTitle or "sharia" in rowTitle or "shariah" in rowTitle or "shariat" in rowTitle:
		islambkList.append(row)


for row in initialList:
	rowTitle = row[0]
	if "online banking" in rowTitle or "digital" in rowTitle or "m commerce" in rowTitle or "m-commerce" in rowTitle or "fintech" in rowTitle or "online" in rowTitle or "internet" in rowTitle or "mobile banking" in rowTitle or "mobile" in rowTitle:
		onlinebkList.append(row)	


for row in initialList:
	rowTitle = row[0]
	if "RBI" in rowTitle or "probe" in rowTitle or "sebi" in rowTitle or "rule" in rowTitle or "licence" in rowTitle or "permit" in rowTitle or "basel" in rowTitle or "governance" in rowTitle or "IMF" in rowTitle or "bailout" in rowTitle or "regulator" in rowTitle or "government" in rowTitle or "federal" in rowTitle or "federal reserve" in rowTitle or "privatisation" in rowTitle or "privatization" in rowTitle or "bank of England" in rowTitle or "central bank" in rowTitle or "law" in rowTitle or "regualtion" in rowTitle:
		regulatList.append(row) 


print("Collaboration: ",len(collabList))
print("expansion: ",len(expanList))
print("fintech: ",len(fintecList))
print("investment: ",len(investList))
print("islamic banking: ",len(islambkList))
print("online banking: ", len(onlinebkList))
print("regualtions: ", len(regulatList))

sumIndexed  = len(collabList)+len(expanList)+len(fintecList)+len(investList)+len(islambkList)+len(onlinebkList)+len(regulatList)

print("Total Indexed: ",sumIndexed)



for cItem in collabList:
	cItem.append("Collaboration")
for eItem in expanList:
	eItem.append("Expansion")
for fItem in fintecList:
	fItem.append("Fintech")
for iItem in investList:
	iItem.append("Investments")
for isItem in islambkList:
	isItem.append("Islamic Banking")
for oItem in onlinebkList:
	oItem.append("Online Banking")
for rItem in regulatList:
	rItem.append("Regulations")


trendList = collabList+expanList+fintecList+investList+islambkList+onlinebkList+regulatList

#checking company name

for trendListItem in trendList:
	trendListTitle = trendListItem[0]
	tokens = nltk.word_tokenize(trendListTitle)
	posTags = nltk.pos_tag(tokens)
	pT = [ ]
	for posTag in posTags:
		# print(posTag)
		if posTag[1] == 'NNP':
			pT.append(posTag[0])

	newsComp = " ".join(str(x) for x in pT)
	nsc = (newsComp)
	trendListItem.append(nsc)



print(trendList[0])
abcList = trendList[4:6]
print (abcList)



#Matching Geo

for linkToRead in abcList:
	yoLink = linkToRead[1]
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]
	html = opener.open(yoLink)
	soup = BeautifulSoup(html.read(), "html5lib")
	[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
	visible_text = soup.getText()

	textTokens = nltk.word_tokenize(visible_text)
	textTags = nltk.pos_tag(textTokens)
	geoTagList = [ ]
	for oneTag in textTags:
		if oneTag[1] == 'NNP':
			geoTagList.append(oneTag[0])
	shortGList = geoTagList [0:80]

	geoDBfile = open('geodata.csv', encoding="utf8")
	georeader = csv.reader(geoDBfile)
	geoDataset = list(georeader)

	citylist = [ ]
	for cityD in geoDataset:
		citz = cityD[0]
		citylist.append(citz)
		couZ = cityD[1]
		citylist.append(couZ)
		statZ = cityD[2]
		citylist.append(statZ)

	theFind = set(shortGList) & set(citylist)
	findList = [ ]
	for findA in theFind:
		findList.append(findA)

	abcList.append(findA)
	time.sleep(10)



	
print (abcList[1])






#Export CSV
with open("junej2.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = '#')
    
    for val in abcList:
    	writer.writerow(val)

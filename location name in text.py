import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tag import pos_tag
import geocoder

#get and read the URL
url = ("http://www.livemint.com/Companies/LgALAZP4F8a0DPnMYuJVgN/RBI-should-give-out-at-least-35-bank-licences-a-year-for-ne.html")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]

html = opener.open(url)
bsObj = BeautifulSoup(html.read(), "html5lib")
obtext = bsObj.findAll('p')
#print(obtext)

t = str(obtext)


tokens = nltk.word_tokenize(t)
#print (tokens)

posTags = nltk.pos_tag(tokens)
pT = [ ]
for posTag in posTags:
	#print(posTag)
	if posTag[1] == 'NNP':
		posTagOne = posTag[0]
		regexName = re.compile(r'[A-Z]+[a-z]+')
		nnpList = regexName.search(posTagOne)

		if nnpList == True: 
			#pT.append(nnpList)
			print(nnpList)
		else:
			pass




#x = " ".join(str(x) for x in pT)
#print (pT)







'''

regexName = re.compile(r'[A-Z]+[a-z]+')
nnpList = regexName.findall(t)

for nnpOne in nnpList:
	g = geocoder.google(nnpOne)
	a = g.country_long

	print([nnpOne,a])

'''

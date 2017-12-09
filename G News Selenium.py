from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

driver = webdriver.Firefox()
driver.get("https://www.google.com/webhp?hl=en#q=education&hl=en&tbs=qdr:y,sbd:1&tbm=nws")

html = driver.page_source    
bsObj = BeautifulSoup(html, "html5lib")

itmes  = bsObj.findAll("h3",{"class":"r _U6c"})

listOne = [ ] #this creates a list of results of the first page. 
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
print("Results on first page: ",len(listOne))


i = 10
for i in range(10,2010,10):
	newlink  = "https://www.google.com/search?q=education&hl=en&biw=1366&bih=669&site=webhp&tbs=qdr:y,sbd:1&tbm=nws&ei=MUZHV9TCMsTxvATV4aTADQ&start="+str(i)+"&sa=N"
	driver = webdriver.Firefox()
	driver.get(newlink)



	try:
		newhtml = driver.page_source

		recursiveBSObj = BeautifulSoup(newhtml.read(), "html5lib")		
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
			listOne.append(stuffTwo)
			#print(listTwo)
			print (len(listOne))
	

	except :
		pass





	i = i+10




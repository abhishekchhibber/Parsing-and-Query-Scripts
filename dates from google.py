import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#get and read the URL
url = ("https://www.google.com/search?q=banking&num=100&espv=2&biw=1366&bih=609&tbs=qdr:m,sbd:1&tbm=nws&source=lnt&sa=X&ved=0ahUKEwi_2o3ym-3MAhUDNI8KHQNPDR8QpwUIFQ&dpr=1")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0")]

html = opener.open(url)
bsObj = BeautifulSoup(html.read(), "html5lib")


#extracting dates of all the links 
itmes  = bsObj.findAll("span",{"class":"f nsa _uQb"})
for item in itmes:
	print(item.text)
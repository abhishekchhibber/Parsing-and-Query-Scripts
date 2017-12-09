import urllib
import urllib.request
import urllib.parse
import re


iList = input('list, seperated by commas, starting with http/s: ') #initial list
lList = iList.split(',') #string converted to list
nList = len(lList) #number in a list

#print (lList)
print ('Total URLs to be searched: '+ str(nList))

for url in lList:
    
    values = {'s': 'basics',
              'submit': 'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    text = str(respData)
    #print(respData)
    eRegex = re.compile(r'[a-zA-Z._0-9]+@\w+\.[a-zA-Z._0-9]+')
    result = eRegex.findall(text) 
    coolResult = '\n'.join(result) 
    print(coolResult)

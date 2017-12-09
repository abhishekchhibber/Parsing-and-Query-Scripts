import urllib
import urllib.request
import urllib.parse
import re

url = input('enter URL: ')
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

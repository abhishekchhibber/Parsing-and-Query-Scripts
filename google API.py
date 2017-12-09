import urllib.request as ur
import json
import csv

with open('toronto_eateries_one.csv', encoding="utf8") as csvfile:
	reader = csv.DictReader(csvfile)
	records = [ ]
	for row in reader:
		records.append(row)


def post_extract (url):	
	html = ur.urlopen(url).read()
	data = json.loads(html.decode('utf-8'))

	a =  (data['results'][0]['address_components'])
	for b in a:
		# print (b)
		try:
			c = b['types']
			if c == ['postal_code']:
				the_code = b['long_name']
				record['postal_code'] = the_code
		except Exception as e:
			pass
	return


for record in records:
	lat = str(record['latitude'])
	lng = str(record['longitude'])
	# print (lat,lng)

	api_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lng+"&key=AIzaSyCdrvDWKcDOBE9AqiQ1NAvuJpUyQ7vMySA"
	post_extract (api_url)


# for t in records:
# 	print (t)

#export csv
with open('te_one.csv', 'w', encoding='utf-8', newline = '') as csvfile: #change here
    fieldnames = ['latitude','longitude','amenity','name','postal_code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()
    for val in records:
    	writer.writerow(val)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import time

MainList =[ ]
with open('cross_country_full.csv') as csvfile: #change here
	reader = csv.DictReader(csvfile)
	acts = [ ]
	for row in reader:
		acts.append(row)
driver = webdriver.Chrome('E:\software\chromedriver')
#driver = webdriver.Firefox()
driver.get('https://collegecoachesonline.com/login.php')
time.sleep(3)
username = driver.find_element_by_name('member_name')
username.send_keys("koolblaze")
password = driver.find_element_by_name('password')
password.send_keys("TestServer")

driver.find_element_by_name("submit").click()




	# driver = webdriver.PhantomJS('E:\software\phantomjs-2.1.1-windows\bin\phantomjs.exe')


for act in acts:
	actLinkHalf = act['link']
	actLink = "https://collegecoachesonline.com/"+actLinkHalf
	actName = act['college_name']
	driver.get(actLink)
	time.sleep(2)

	College_Name = actName

	colName = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]").text
	colSite = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/a").text
	colPhone = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]").text
	colSport = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[1]/table/tbody/tr[1]/td[2]").text
	colCoach = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[1]/table/tbody/tr[2]/td[2]").text
	colCoachEmail = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[1]/table/tbody/tr[3]/td[2]/a").text
	colCoachPhone = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[1]/table/tbody/tr[4]/td[2]").text
	colDivision = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/table/tbody/tr[1]/td[2]").text
	colRegion = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[2]").text
	colConf = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/table/tbody/tr[3]/td[2]").text
	colNickname = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td[2]").text
	colAthSite = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/table/tbody/tr[5]/td[2]/a").text
	colSchoolType = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[6]/td[1]/table/tbody/tr[1]/td[2]").text
	colCostInState = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[6]/td[1]/table/tbody/tr[2]/td[2]").text
	colCostOutState = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[6]/td[1]/table/tbody/tr[3]/td[2]").text
	colRating = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[6]/td[2]/table/tbody/tr[1]/td[2]").text
	colEnrollment = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td[2]").text


	colResults = dict([('College Name', College_Name), ('College Name/add', colName), ('Website', colSite), ('Main Phone', colPhone), ('Type of Sport', colSport), ('Coach Name', colCoach), ('Coach Email', colCoachEmail), ('Coach Phone', colCoachPhone), ('Division', colDivision), ('Region', colRegion), ('Conference', colConf), ('Nickname/Mascot', colNickname), ('Athletic Website', colAthSite), ('Type of School', colSchoolType), ('Tuition Cost - In State', colCostInState), ('Tuition Cost - Out of State', colCostOutState), ('Academic Rating', colRating), ('School Enrollment', colEnrollment)])
	MainList.append(colResults)
	time.sleep(1)
	

	print (len(MainList))
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
driver.close()
with open('cross_country_extracted.csv', 'w', encoding='utf-8', newline = '') as csvfile: #change here
    fieldnames = ['College Name', 'College Name/add', 'Website', 'Main Phone', 'Type of Sport', 'Coach Name', 'Coach Email', 'Coach Phone', 'Division', 'Region', 'Conference', 'Nickname/Mascot', 'Athletic Website', 'Type of School', 'Tuition Cost - In State', 'Tuition Cost - Out of State', 'Academic Rating', 'School Enrollment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()
    for val in MainList:
    	writer.writerow(val)

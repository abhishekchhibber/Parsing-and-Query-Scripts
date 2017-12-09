from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Firefox()
browser.get("https://mail.google.com/mail/u/2/?tab=wm#inbox")
email = browser.find_element_by_id("Email")
email.send_keys("indinsightz@gmail.com")
nextOne = browser.find_element_by_id("next")
nextOne.click()

 

try:
    waitOne = WebDriverWait(browser, 10).until(
    	EC.presence_of_element_located((By.ID, "Passwd"))
    )
except:
	print ("Check, it's not working!")

pwd = browser.find_element_by_id("Passwd")
pwd.send_keys("abhi1206")
signIn = browser.find_element_by_id("signIn")
signIn.click()

try:
    waitTwo = WebDriverWait(browser, 10).until(
    	EC.presence_of_element_located((By.ID, "gbqfq"))
    )
except:
	print ("Check, it's not working!")
sear = browser.find_element_by_id("gbqfq")
sear.send_keys("label:unread")
serBut = browser.find_element_by_id("gbqfb")
serBut.click()


inInbox = input("Click on the first message and enter 'y': ")
if inInbox == "y":
	

else:
	print ("Please confirm if you are inside the inbox")
cURL = browser.current_url
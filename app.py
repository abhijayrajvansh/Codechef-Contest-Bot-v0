from ast import excepthandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By

import os
import datetime
import time

pwd = "/Users/abhijayrajvansh/Downloads"
PATH = Service(pwd + "/chromedriver")

# url to be launched ...
url = "https://www.codechef.com/problems-old/PRACLIST"

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")
# chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
# driver.maximize_window()
# driver.minimize_window()

driver.get(url) # launches the broswer and open url


# Building Testcase Downloader

for i in range(1, 5 + 1):

	CUSTOM_XPATH = "//span[@id='sample-" + "input" + "-" + str(i) + "']//pre[contains(@class,'mathjax-support')]"

	try:
		sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH).text
		print(sample_testcases)
		print()
	except:
		print("No further Testcases was found!")
		break

	CUSTOM_XPATH = "//span[@id='sample-" + "output" + "-" + str(i) + "']//pre[contains(@class,'mathjax-support')]"

	sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH).text
	print(sample_testcases)
    



from curses.ascii import isalnum, isdigit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By
import os

pwd = "/Users/abhijayrajvansh/Downloads"
PATH = Service(pwd + "/chromedriver")

# URL to be launched ...
URL = "https://www.codechef.com/problems-old/PRACLIST"

CODECHEF_URL = "https://www.codechef.com/"

# CC Type to accept in argument
url_cc_data = "LTIME108D"

sample_url = "https://www.codechef.com/" + url_cc_data

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")
# chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
# driver.maximize_window()
# driver.minimize_window()

test_url1 = "https://www.codechef.com/LTIME108D"
test_url2 = "https://www.codechef.com/START47D"
test_url3 = "https://www.codechef.com/COOK143D"
test_url4 = "https://www.codechef.com/JULY221D"

driver.get(test_url4) # launches the broswer and open URL

CONTEST_TYPE = "" #DONE 

for i in url_cc_data:
    if i.isdigit():
        break
    if i.isalpha():
        CONTEST_TYPE += i


CC_Path = "/Users/abhijayrajvansh/Desktop/codechef/" + CONTEST_TYPE

try : 
    os.mkdir(CC_Path)
except FileExistsError:
    print(end="")

total_prob = 0

all_prb_xpath = "//body/div[@id='ember-root']/div[@id='ember256']/main[@class='contest-container content']/section[@class='content-area small-8 columns pl0']/div[2]"
prbdata = driver.find_element(By.XPATH, all_prb_xpath).text

all_problem_data = []
value = ""

for i in prbdata:
    if i == '\n':
        all_problem_data.append(value)
        value = ""
    value += i

print(all_problem_data)
# To be continued...

# Building Testcase Downloader
def download_testcases():

    for i in range(1, 5 + 1):
        
        try:
            CUSTOM_XPATH_IN = "//span[@id='sample-" + "input" + "-" + str(i) + "']//pre[contains(@class,'mathjax-support')]"
            sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH_IN).text
            print(sample_testcases)
            print()
            CUSTOM_XPATH_OT = "//span[@id='sample-" + "output" + "-" + str(i) + "']//pre[contains(@class,'mathjax-support')]"
            sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH_OT).text
            print(sample_testcases)
            print()

        except:
            print("No further Testcases was found!")
            break

        
# download_testcases()
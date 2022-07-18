from curses.ascii import isalnum, isalpha, isdigit
from email import contentmanager
from random import sample
from time import sleep
from typing import final
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By
import os
import sys
import subprocess

pwd = "/Users/abhijayrajvansh/Downloads"
PATH = Service(pwd + "/chromedriver")

# MULTIPLE_TT_ to be launched ...
# MULTIPLE_TT_URL = "https://www.codechef.com/problems-old/PRACLIST"

CODECHEF_URL = "https://www.codechef.com/"

# CC Type to accept in argument
url_cc_data = sys.argv[1]

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")
# chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
# driver.maximize_window()
# driver.minimize_window()

CONTEST_URL = "https://www.codechef.com/" + url_cc_data + "D"
print("Looking for " + CONTEST_URL)

driver.get(CONTEST_URL) # launches the broswer and open MULTIPLE_TT_

CONTEST_TYPE = url_cc_data


CC_Path = "/Users/abhijayrajvansh/Desktop/codechef/" + CONTEST_TYPE + "/"

try : 
    os.mkdir(CC_Path)
    print("\nCreating " + url_cc_data + " Directory...")
except FileExistsError:
    print(end="")

all_prb_xpath = "//body/div[@id='ember-root']/div[@id='ember256']/main[@class='contest-container content']/section[@class='content-area small-8 columns pl0']/div[2]"
prbdata = driver.find_element(By.XPATH, all_prb_xpath).text

all_problem_data = []
value = ""

for i in prbdata:
    if i == '\n':
        all_problem_data.append(value)
        value = ""
    value += i

final_data = []
k = 0

for i in range(2, len(all_problem_data)):
    final_data.append(all_problem_data[i])

problem_code = []

for i in range(0, len(final_data), 4):
    problem_code.append(final_data[i+1])


# #To be updated with live contest pre url of contest of each problem
PRB_URL = "https://www.codechef.com/problems-old/"

total_problems = len(problem_code)

print("\nTotal problems found:", total_problems, "\n")
print("All Problems Code: ", problem_code, "\n")


def total_testcases():
    count = 0
    for i in range(1, 5 + 1):
        try:
            CUSTOM_XPATH_IN = "//span[@id='sample-" + "input" + "-" + str(i) + "']//pre[contains(@class,'mathjax-support')]"
            sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH_IN).text
            count += 1
        except:
            break
    
    return count


# Building Testcase Downloader
def download_testcases(pb_code):
    total_tc = total_testcases()
    print("Total Testcases found: ", total_tc)

    for tc_num in range(1, total_tc + 1):

        strtc = str(tc_num)
        CUSTOM_XPATH_IN = "//span[@id='sample-" + "input" + "-" + strtc + "']//pre[contains(@class,'mathjax-support')]"
        sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH_IN).text

        arr = []     
        temp = ""

        sample_testcases += "\nAbhijay Rajvansh" # Edge testcases haha real life example

        for i in sample_testcases:
            if i == '\n':
                arr.append(temp)
                temp = ""
            else:
                temp += i

        curr_prob_path = CC_Path + pb_code
        print("Saving Testcase No:", strtc, "\n")

        

        try : 
            os.mkdir(curr_prob_path)
        except FileExistsError:
            print(end="")

        solution_file_path = curr_prob_path + "/" + pb_code + ".cpp"
        solution_file = open(solution_file_path, "w")
        subprocess.run(["code", solution_file_path])


        with open(curr_prob_path + "/sample_input_" + strtc + ".txt", "w") as tc_file:
            for line in arr:
                tc_file.write(line + '\n')


        CUSTOM_XPATH_OT = "//span[@id='sample-" + "output" + "-" + strtc + "']//pre[contains(@class,'mathjax-support')]"
        sample_testcases = driver.find_element(By.XPATH, CUSTOM_XPATH_OT).text

        arr = []     
        temp = ""

        sample_testcases += "\nAbhijay Rajvansh" # Edge testcases haha real life example

        for i in sample_testcases:
            if i == '\n':
                arr.append(temp)
                temp = ""
            else:
                temp += i

        curr_prob_path = CC_Path + pb_code

        try : 
            os.mkdir(curr_prob_path)
        except FileExistsError:
            print(end="")


        with open(curr_prob_path + "/sample_output_" + strtc + ".txt", "w") as tc_file:
            for line in arr:
                tc_file.write(line + '\n')


for i in range(total_problems): #1 -> total_problems
    curr_pb_code = problem_code[i]
    pb_code = ""
    for i in range(1, len(curr_pb_code)):
        pb_code += curr_pb_code[i]

    
    print("Looking testcases for: ", PRB_URL + pb_code, "\n")
    driver.get(PRB_URL + pb_code)

    sleep(3)
    download_testcases(pb_code)
    sleep(1)
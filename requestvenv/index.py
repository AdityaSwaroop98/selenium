from cgitb import text
from cmath import log
import imp
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from typing import ItemsView
from bs4 import BeautifulSoup
import pandas as pd
from webbrowser import Chrome, get
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import requests
import gspread
import operator
import json
import csv

chromeOptions = Options()

chrome_path = "../SeleniumDrivers/chromedriver"
driver = webdriver.Chrome(chrome_path)

url = "https://state.bihar.gov.in/main/CitizenHome.html"
driver.get(url)
# driver.minimize_window()
wait = WebDriverWait(driver, 7)
scrollDown = "window.scrollBy(0,1000);"
driver.execute_script(scrollDown)
gad_click = wait.until(ec.visibility_of_element_located(
    (By.LINK_TEXT, "General Administration Department")))
gad_click.click()

# switch to new window
driver.switch_to.window(driver.window_handles[1])
# driver.minimize_window()
tnp_click = wait.until(ec.visibility_of_element_located(
    (By.LINK_TEXT, "Transfer & Postings")))
tnp_click.click();

current = driver.current_url

final_click = wait.until(ec.visibility_of_all_elements_located(
    (By.CLASS_NAME, "dtr-details")))

list1 = []
list2 = []

for final in final_click:
    description = final.find_elements(
        by=By.XPATH, value="/html//div/table//tr/td/table/tr[4]/td")
    date = final.find_elements(
        by=By.XPATH, value="/html/body/div[1]/div[2]/div/div[7]/div[2]/div[2]/div//tbody/tr/td/table/tr[2]/td")
for dates in date:
    item = {
        'Date': dates.text,  #
    }
    list1.append(item)

for desc in description:
    item = {
        'Description': desc.text
    }
    list2.append(item)
valuesDate = [i['Date'] for i in list1]
print(valuesDate)
valuesDesc = [i['Description'] for i in list2]
print(valuesDesc)


# GoogleSheet Function 

def output(valuesDate, valuesDesc):
    gc = gspread.service_account(filename='creds.json')
    print(gc)
    sh = gc.open('scraped').sheet1
    cell_value1 = valuesDate
    cell_value2 = valuesDesc
    cell_list1 = sh.range('A1:A10')
    for i, val in enumerate(cell_value1):
        cell_list1[i].value = val
    sh.update_cells(cell_list1)
    cell_list2 = sh.range('B1:B10')
    for i, val in enumerate(cell_value2):
        cell_list2[i].value = val
    sh.update_cells(cell_list2)
    return
output(valuesDate, valuesDesc)

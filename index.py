# import requests

# s = requests.Session()

# payload = {"editForm&rowId" : "2938"}

# sut = 'https://state.bihar.gov.in/gad/SectionInformation.html/cookie/set'

# gut = 'https://state.bihar.gov.in/gad/SectionInformation.html/cookie'

# s.get(sut, params= payload)

# r = s.get(gut)
# print(r.text)






# print(r.text)



# from http.client import OK
# import imp


# import os
# from selenium import webdriver


# os.environ['PATH'] += r"C:/SeleniumDrivers"
# driver = webdriver.Chrome()

# driver.get("https://state.bihar.gov.in/main/CitizenHome.html")

# my_element = driver.find_element_by_partial_link_text("General Administration Department")

# my_element.click()
    
# driver.implicitly_wait(3)
# my_second = driver.find_element_by_link_text('Transfer & Postings')

# my_second.click()








# import os
# from selenium import webdriver
# import time
# os.environ['PATH'] += r"C:/SeleniumDrivers"
# driver = webdriver.Chrome()
# # to maximize the browser window
# driver.maximize_window()
# #get method to launch the URL
# driver.get("https://state.bihar.gov.in/main/CitizenHome.html")
# #to refresh the browser
# # driver.refresh()
# driver.find_element_by_link_text("General Administration Department").click()
# #prints the window handle in focus
# print(driver.current_window_handle)
# #to fetch the first child window handle
# chwnd = driver.window_handles[1]
# #to switch focus the first child window handle
# driver.switch_to.window(chwnd)
# print(driver.find_element_by_link_text("Transfer & Postings").click())
# #to close the browser
# # driver.quit()
# # time.sleep(1)
# chwndi = driver.window_handles[1]
# #to switch focus the first child window handle
# driver.switch_to.window(chwndi)
# print(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[7]/div[2]/div[2]/div/table/tbody/tr[2]/td/table/tr[5]/td/strong/a").click())

# import modules
from selenium import webdriver
import time
import os
from selenium.webdriver.support.select import Select

with open('gov_scrape.csv','w')as file:
    file.write("Description :- \n \n")
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
# # to maximize the browser window
driver.maximize_window()

# assign URL
driver.get("https://state.bihar.gov.in/main/CitizenHome.html")
print("First window title = " + driver.title)

# switch to new window
driver.find_element_by_link_text("General Administration Department").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
print("Second window title = " + driver.title)

# switch to new window
driver.find_element_by_link_text("Transfer & Postings").click()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
# a = driver.find_element_by_class_name("sorting")
# print(a.__str__())
# print(driver.title)
#//table[@id="dataTableResponsive"]//tr[@class="parent odd"]/td[5]   //table[@id="dataTableResponsive"]//tr[4]/td    //table[@class="dtr-details"]//tr[4]

desc = driver.find_elements_by_xpath('//table[@id="dataTableResponsive"]//tr[@class="parent odd"]/td[5]')
# for descs in desc:
#     print(str(descs.text)) 
with open('gov_scrape.csv','a')as file:
    for i in range(len(desc)):
     file.write(desc[i].text + "\n")
































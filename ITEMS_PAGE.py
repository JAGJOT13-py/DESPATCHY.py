import logging
import time
from random import random

# import filepath as filepath
# from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
# Python3 code to select
# data from excel
import xlwings as xw

# Specifying a sheet
ws = xw.Book("Book1.xlsx").sheets['Sheet1']

# Selecting data from
# a single cell
v1 = ws.range("E1:E4").value
# v2 = ws.range("F1:F4").value
v2 = [12, 13, 14, 15]
# v3 = ws.range("C1:C2").value
print("Result:", v1, v2)

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get("https://brizdev.solve8.com.au/login")
time.sleep(3)

driver.find_element("xpath", '//*[@id="email"]').send_keys("admin@example.com")
time.sleep(2)

driver.find_element("xpath",
                    '/html/body/div[2]/section/div/div[1]/div/div/div/div/form/div[1]/div[2]/div/input').send_keys(
    "password")
time.sleep(2)

driver.find_element("xpath", '/html/body/div[2]/section/div/div[1]/div/div/div/div/form/div[2]/button').click()
time.sleep(2)

# for navigating to business drop down menu
a = ActionChains(driver)
u = driver.find_element("xpath", '//*[@id="navbarDropdown"]')
a.move_to_element(u).perform()
time.sleep(2)
# for clicking on item
driver.find_element("xpath", '//*[@id="navbar_main"]/div/ul/li[4]/ul/li[3]/a/span').click()
time.sleep(2)

# for creating new item
driver.find_element("xpath", '/html/body/main/div[2]/div/div/div/div/div[1]/div[2]/a').click()
time.sleep(2)

# for filling details of new item
for iname, icode in zip(v1, v2):
    try:
        try:
            driver.find_element("xpath", '/html/body/main/div[2]/div/div/div/div/div[1]/div[2]/a').click()
            time.sleep(2)
        except:
            time.sleep(2)

        driver.find_element("xpath", '//*[@id="name"]').clear()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="name"]').send_keys(iname)
        time.sleep(2)
        driver.find_element("xpath", '//*[@id="code"]').clear()
        time.sleep(2)
        try:
            driver.find_element("xpath", '/html/body/div[3]/div/div[6]/button[1]').click()
            time.sleep(2)
        except:
            time.sleep(2)
        driver.find_element("xpath", '//*[@id="code"]').send_keys(icode)
        time.sleep(2)
        driver.find_element("xpath",
                            '/html/body/main/div[2]/div/form/div/div/div/div[2]/div/div[1]/div[12]/div/select').click()
        time.sleep(2)
        try:
            driver.find_element("xpath", '/html/body/div[3]/div/div[6]/button[1]').click()
            time.sleep(2)
        except:
            time.sleep(2)
        driver.find_element("xpath",
                            '/html/body/main/div[2]/div/form/div/div/div/div[2]/div/div[1]/div[12]/div/select').click()
        time.sleep(2)
        driver.find_element("xpath",
                            '/html/body/main/div[2]/div/form/div/div/div/div[2]/div/div[1]/div[12]/div/select/option[2]').click()
        time.sleep(2)
        driver.find_element("xpath",
                            '/html/body/main/div[2]/div/form/div/div/div/div[2]/div/div[2]/button').click()
        time.sleep(2)


    except:
        driver.save_screenshot("screenshot.png")
        logging.basicConfig(filename="logfilename.log", level=logging.INFO)

        logging.info('Something went wrong with %s', iname)
        logging.error('Item cannot be created')
        logging.debug('DEBUGGING')

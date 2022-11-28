import logging
import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
# Python3 code to select data from excel
import xlwings as xw

# Specifying a sheet
ws = xw.Book("Book1.xlsx").sheets['Sheet1']

# Selecting data from
# a single cell
# v1 = ws.range("A1:A4").value
v1 = ["sdfsdf", "dffsdfsd", "XZCxZCzx", "ascascasc"]
#v2 = ws.range("B1:B4").value
v2 = ["sdgsg", "sdfsfgs", "fhftgh", "nvmghj"]
# v3 = ws.range("C1:C4").value
v3 = ["jotsingh1@mailinator.com", "hari@mail.com", "sita@mail.com", "honeysingh@mail.com"]
# v4 = ws.range("D1:D4").value
v4 = [123123, 131313123,31231233, 123123123]
print("Result:", v1, v2)

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get("https://brizdev.solve8.com.au/login")
time.sleep(5)

driver.find_element("xpath", '//*[@id="email"]').send_keys("admin@example.com")
time.sleep(5)

driver.find_element("xpath",
                    '/html/body/div[2]/section/div/div[1]/div/div/div/div/form/div[1]/div[2]/div/input').send_keys(
    "password")
time.sleep(2)

driver.find_element("xpath", '/html/body/div[2]/section/div/div[1]/div/div/div/div/form/div[2]/button').click()
time.sleep(5)

# for navigating to business drop down menu
a = ActionChains(driver)
u = driver.find_element("xpath", '//*[@id="navbarDropdown"]')
a.move_to_element(u).perform()
time.sleep(5)
# for clicking on user
driver.find_element("xpath", '//*[@id="navbar_main"]/div/ul/li[4]/ul/li[1]/a/span').click()
time.sleep(5)

# for creating new user
driver.find_element("xpath", '/html/body/main/div[2]/div/div/div/div/div[1]/div[2]/a').click()
time.sleep(5)

# for filling details of new user
for fname, lname, gmail, mobno in zip(v1, v2, v3, v4):
    try:
        driver.find_element("xpath", '//*[@id="first_name"]').clear()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="first_name"]').send_keys(fname)
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="last_name"]').clear()
        time.sleep(4)
        driver.find_element("xpath", '//*[@id="last_name"]').send_keys(lname)
        time.sleep(4)
        driver.find_element("xpath", '//*[@id="email"]').clear()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="email"]').send_keys(gmail)
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="mobno"]').click()
        time.sleep(3)
        try:
            driver.find_element("xpath", '/html/body/div[4]/div/div[6]/button[1]').click()
            time.sleep(3)
        except:
            time.sleep(3)

        driver.find_element("xpath", '//*[@id="mobno"]').clear()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="mobno"]').send_keys(mobno)
        time.sleep(3)
        # for selecting user role
        driver.find_element("xpath", '//*[@id="role_id"]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="role_id"]/option[3]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="customer_id"]').click()
        time.sleep(3)
        driver.find_element("xpath", '//*[@id="customer_id"]/option[6]').click()
        time.sleep(3)
        driver.find_element("xpath", '/html/body/main/div[2]/div/form/div/div[2]/div/div[2]/div/div[2]/button').click()
        time.sleep(3)
    except:
        driver.save_screenshot('screenshot.png')
        logging.basicConfig(filename="logfilename.log", level=logging.INFO)

        logging.info('Something went wrong')
        logging.error('User cannot be created')
        logging.debug('DEBUGGING')

#        driver.save_screenshot('screenshot.png')
#        driver.find_element("xpath", '/html/body/div[4]/div/div[6]/button[1]').click()
#        time.sleep(3)


#    driver.find_element("xpath", '//*[@id="mobno"]').send_keys("123456789")
#    time.sleep(3)

# for selecting user role
# driver.find_element("xpath", '//*[@id="role_id"]').click()
# time.sleep(5)
# driver.find_element("xpath", '//*[@id="role_id"]/option[3]').click()
# time.sleep(5)
# driver.find_element("xpath", '//*[@id="customer_id"]').click()
# time.sleep(5)
# driver.find_element("xpath", '//*[@id="customer_id"]/option[6]').click()
# time.sleep(5)
# for submit button
# driver.find_element("xpath", '/html/body/main/div[2]/div/form/div/div[2]/div/div[2]/div/div[2]/button').click()
# time.sleep(5)

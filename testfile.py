import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver.exe')
driver.maximize_window()
driver.get("https://brizdev.solve8.com.au/login")
time.sleep(2)
print("PAGE OPENED SUCCESSFULLY")
driver.find_element("xpath", '//*[@id="email"]').send_keys("admin@example.com")
time.sleep(4)
print("EMAIL FILLED SUCCESSFULLY")
driver.find_element("xpath",
                    '/html/body/div[2]/section/div/div[1]/div/div/div/div/form/div[1]/div[2]/div/input').send_keys(
    "password")
time.sleep(2)
print("PASSWORD FILLED SUCCESSFULLY")

driver.find_element("xpath", '/html/body/div[2]/section/div/div[1]/div/div/div/div/form/div[2]/button').click()
time.sleep(4)
print("DESPATCHY OPENED SUCCESSFULLY")
# for booking of new user as customer
driver.find_element("xpath", '//*[@id="navbar_main"]/div/ul/li[1]/a/span').click()
time.sleep(4)
print("BOOKING OPENED SUCCESSFULLY")
# for scrolling down by pixels
# driver.execute_script("window.scrollBy(0,1000)")
driver.find_element("xpath", '//*[@id="nav_pending"]/div/div/div/div[2]/div/div[1]/div/a').click()
time.sleep(4)
# for booking details
driver.find_element("xpath", '//*[@id="customer"]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="customer"]/option[6]').click()
time.sleep(4)
# for consignment type as Pickup
driver.find_element("xpath", '//*[@id="pickup"]').click()
time.sleep(4)
# for sender selection
driver.find_element("xpath", '//*[@id="sender"]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="sender"]/option[2]').click()
time.sleep(4)
# for receiver selection
driver.find_element("xpath", '//*[@id="receiver"]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="receiver"]/option[3]').click()
time.sleep(4)
# for selecting items
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(4)
driver.find_element("xpath", '//*[@id="select2-item_1-container"]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="item_1"]/option[2]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="quantity_1"]').clear()
time.sleep(3)
driver.find_element("xpath", '//*[@id="quantity_1"]').send_keys("3")
time.sleep(3)

# for submit button
driver.find_element("xpath", '//*[@id="btn-submit-booking"]').click()
time.sleep(4)

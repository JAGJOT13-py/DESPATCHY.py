import time

from select import select
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
v1 = ws.range("A1:A4").value
v2 = ws.range("B2").value
v3 = ws.range("C1:C2").value
v4 = ws.range("D1:D2").value
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
# a = ActionChains(driver)
# u = driver.find_element("xpath", '//*[@id="navbarDropdown"]')
# a.move_to_element(u).perform()
# time.sleep(5)
# for clicking on user
# driver.find_element("xpath", '//*[@id="navbar_main"]/div/ul/li[4]/ul/li[1]/a/span').click()
# time.sleep(5)

# for creating new user
# driver.find_element("xpath", '/html/body/main/div[2]/div/div/div/div/div[1]/div[2]/a').click()
# time.sleep(5)

# for filling details of new user
#for x in v1:
    #try:
# driver.find_element("xpath", '//*[@id="first_name"]').send_keys("x")
# time.sleep(5)
#driver.find_element("xpath", '//*[@id="first_name"]').clear()
# time.sleep(5)
    #except:
# driver.save_screenshot('screenshot.png')

#for x in v2:
    #try:
# driver.find_element("xpath", '//*[@id="last_name"]').send_keys("y")
# time.sleep(5)
#    except:
# driver.save_screenshot('screenshot.png')
#
# for x in v3:
#    try:
#        driver.find_element("xpath", '//*[@id="email"]').send_keys(x)
#        time.sleep(4)
#        driver.find_element("xpath", '/html/body/div[4]/div/div[6]/button[1]').click()
#        time.sleep(3)
#    except:
#        driver.save_screenshot('screenshot.png')
#        driver.find_element("xpath", '/html/body/div[4]/div/div[6]/button[1]').click()
#        time.sleep(3)
# for x in v4:
#    try:
#
#        driver.find_element("xpath", '//*[@id="mobno"]').send_keys(x)
#        time.sleep(3)
#        driver.find_element("xpath", '/html/body/main/div[2]/div/form/div/div[2]/div/div[2]/div/div[2]/button').click()
#        time.sleep(5)
#    except:
#        driver.save_screenshot('screenshot.png')
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

# for booking of new user as customer
driver.find_element("xpath", '//*[@id="navbar_main"]/div/ul/li[1]/a/span').click()
time.sleep(4)
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
# for consignment type as Delivery
# driver.find_element("xpath", '//*[@id="delivery"]').click()
# time.sleep(4)
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
# for instruction pickup
driver.find_element("xpath", '//*[@id="booking_form"]/div/div/div[1]/div[2]/div/div[1]/div[7]/div/button[1]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="pickup_name"]').send_keys("any name")
time.sleep(4)
driver.find_element("xpath", '//*[@id="pickup_phone"]').send_keys("123456789")
time.sleep(4)
driver.find_element("xpath", '//*[@id="pickup_note"]').send_keys("any note")
time.sleep(4)
driver.find_element("xpath", '//*[@id="pickup_call"]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="btn-save-pickupinstruction"]').click()
time.sleep(4)
# for instruction delivery
# driver.find_element("xpath", '//*[@id="booking_form"]/div/div/div[1]/div[2]/div/div[1]/div[7]/div/button[2]').click()
# time.sleep(4)
# driver.find_element("xpath", '//*[@id="delivery_name"]').send_keys("any name")
# time.sleep(4)
# driver.find_element("xpath", '//*[@id="delivery_phone"]"]').send_keys("any number")
# time.sleep(4)
# driver.find_element("xpath", '//*[@id="delivery_note"]').send_keys("any note")
# time.sleep(4)
# driver.find_element("xpath", '//*[@id="delivery_call"]').click()
# time.sleep(4)
# driver.find_element("xpath", '//*[@id="btn-save-deliveryinstruction"]').click()
# time.sleep(4)

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
# driver.find_element("xpath", '//*[@id="terms_condition"]').click()
time.sleep(4)
driver.find_element("xpath", '//*[@id="btn-submit-booking"]').click()
time.sleep(4)

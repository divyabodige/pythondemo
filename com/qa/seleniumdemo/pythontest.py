from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.freecrm.com")
title = driver.title
print(title)
assert "#1 Free CRM software in the cloud for sales and service" in title
driver.find_element_by_name("username").send_keys("divya")
driver.find_element_by_name("password").send_keys("test12345")
driver.close()
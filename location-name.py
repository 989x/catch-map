from selenium import webdriver
import time
import json

maplink = "https://goo.gl/maps/W9hZEZWKUyvMYQFU6"

driver = webdriver.Chrome()

driver.get(maplink)

location_name_element = driver.find_element("css selector", ".DUwDvf.fontHeadlineLarge")
location_name = location_name_element.text

print(location_name)

with open('location.json', 'w') as f:
    json.dump({"name": location_name}, f)

time.sleep(10)
driver.quit()

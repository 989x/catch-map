from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# maplink = "https://goo.gl/maps/TRXPjnvGDLfCdQZa7"
# "name": "เดอะ เรสซิเดนซ์ แอท แมนดาริน โอเรียนเต็ล กรุงเทพฯ",

maplink = "https://goo.gl/maps/RTKkhsHXwLeHAGFE9"
# "name": "โรงแรมโฟร์ซีซันส์ กรุงเทพฯ แอท เจ้าพระยาริเวอร์",

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

title = driver.get(maplink)

location_name_element = driver.find_element("css selector", ".DUwDvf.fontHeadlineLarge")
location_name = location_name_element.text
print(location_name)

# Find and click the "Nearby" button
nearby_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='g88MCb S9kvJb ' and @jsaction='pane.placeActions.nearby;keydown:pane.placeActions.nearby']")))
nearby_btn.click()

# Wait for search results to load and click on the first one
search_restaurants = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='gridcell' and @class='DgCNMb']")))
search_restaurants.click()

# Wait for search results to load and extract the first three results' aria-label
search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='hfpxzc']")))
results_json = []
for i, result in enumerate(search_results[:5]):
    result_json = {"index": i+1, "label": result.get_attribute("aria-label")}
    results_json.append(result_json)

print(results_json)



# _________________________ doing find nearby places from location_name _________________________

# encountered many problems Sometimes the code works. Sometimes it doesn't work

# Wait for the category buttons to load and click on "Restaurant"
category_btns = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Nv2PK THOPZb CpccDe ']")))
category_btns.click()

category_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='g88MCb S9kvJb ']")))
category_btn2.click()

# Wait for the search box to load and fill it in with "New York City"
search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.tactile-searchbox-input")))

# sometimes works Sometimes it doesn't work
search_box.send_keys(location_name)

# button_search = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mL3xi']")))
# button_search.click()

# code don't working
# Press Enter to submit the search query
# search_box.send_keys(Keys.ENTER)

# _________________________ doing find nearby places from location_name _________________________



with open('drop.json', 'w', encoding='utf-8') as f:
    # json.dump({"name": location_name}, f, ensure_ascii=False)
    # json.dump(results_json, f, ensure_ascii=False) 
    json.dump({"name": location_name, "results": results_json}, f, ensure_ascii=False)
    
time.sleep(10)
driver.quit()
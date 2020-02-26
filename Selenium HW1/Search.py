import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('config.json') as f:
        data = json.load(f)
      #  print(data)
x = data["website"]
y = data["search_phrase1"]
wait_time = data["wait_time"]
#print(x)
driver = webdriver.Chrome()
driver.get(x);
#driver.findElement(By.name("q")).sendKeys(y);
elem = driver.find_element_by_name("q")
elem.clear()
time.sleep(wait_time)
elem.send_keys(y)
elem.send_keys(Keys.ENTER)
time.sleep(wait_time)

driver.quit()

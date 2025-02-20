from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Open Amazon website
driver.get("https://www.amazon.com/")

# Maximize the browser window
driver.maximize_window()

# Locate the search bar, enter a query, and search
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Laptop")
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to load results
time.sleep(5)

# Close the browser
driver.quit()

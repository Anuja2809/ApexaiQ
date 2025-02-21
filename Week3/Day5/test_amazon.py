from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_amazon_search():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("Laptop")
    search_box.send_keys(Keys.RETURN)

    assert "Laptop" in driver.page_source
    print("Test Passed: Amazon Search Executed Successfully")
    driver.quit()

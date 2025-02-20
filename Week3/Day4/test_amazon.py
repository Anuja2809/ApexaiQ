import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    """Initialize the WebDriver and quit after the test"""
    driver = webdriver.Chrome()
    driver.maximize_window()  # Maximize the browser window
    yield driver
    driver.quit()

def test_open_amazon(setup):
    """Test case to open Amazon and verify the title"""
    setup.get("https://www.amazon.com/")
    assert "Amazon" in setup.title

def test_search_product(setup):
    """Test case to search for a product on Amazon"""
    setup.get("https://www.amazon.com/")
    
    # Wait for the search box to be clickable and enter the search term
    wait = WebDriverWait(setup, 20)  # Increase timeout to 20 seconds
    search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("Laptop")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to be visible (increased timeout for slower loading)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot")))

    # Ensure that the search results contain "Laptop"
    assert "Laptop" in setup.page_source

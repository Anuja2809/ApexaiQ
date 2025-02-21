import pytest
import logging
from selenium import webdriver

# Configure logging
logging.basicConfig(filename="logs/test_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.fixture
def setup(request):
    """ Fixture to set up WebDriver and handle failures with screenshots """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com")

    # Teardown: Take screenshot if test fails
    def teardown():
        if request.node.rep_call.failed:
            driver.save_screenshot(f"logs/{request.node.name}_failure.png")
        driver.quit()

    request.addfinalizer(teardown)
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Capture test result to handle failure logging """
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)

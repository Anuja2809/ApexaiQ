# Kb Corel Scrapper

#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
# from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options for headless operation (no GUI)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

# Use WebDriver Manager to automatically get the correct ChromeDriver (Optional)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Direct method if you have ChromeDriver installed manually
driver = webdriver.Chrome(options=options)

# Open the Corel Knowledge Base page
driver.get("https://kb.corel.com/en/125936")
time.sleep(1)  # Allow time for page to load

# Locate the first table on the page using XPath
tables = driver.find_element(By.XPATH, ".//table")

# Extract all rows from the table
all_table_rows = tables.find_elements(By.XPATH, ".//tr")

list_of_rows = []

# Loop through each row in the table
for each_row in all_table_rows:
    list_of_data = []
    # Get all cells (columns) in the row
    all_data = each_row.find_elements(By.XPATH, ".//td")
    for data in all_data:
        list_of_data.append(data.text)  # Add text data from each cell
        
    list_of_rows.append(list_of_data)

# Create a pandas DataFrame from the extracted rows
df = pd.DataFrame(list_of_rows[1:], columns=list_of_rows[0])  # Skip the first row as it's headers

# Save the data to a CSV file
df.to_csv("korel.csv", index=False)
print("CSV saved")

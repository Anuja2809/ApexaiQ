import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Open the webpage
driver.get("https://en.wikipedia.org/wiki/Oracle_Linux")
time.sleep(1)

# Function to scrape a table
def scrape_table(xpath):
    try:
        table = driver.find_element(By.XPATH, xpath)
        rows = table.find_elements(By.XPATH, ".//tr")

        headers = [header.text.strip() for header in rows[0].find_elements(By.XPATH, ".//th")]
        
        # Check if headers are extracted
        if not headers:
            print("No headers found.")
            return pd.DataFrame()  # Return empty DataFrame if no headers found

        data = []
        for row in rows[1:]:  # Skip the header row
            cells = row.find_elements(By.XPATH, ".//th | .//td")
            row_data = [cell.text.strip() if cell.text.strip() != '' else '-' for cell in cells]  # Replace empty with '-'
            data.append(row_data)

        # Check if data is empty
        if not data:
            print("No data found in table.")
            return pd.DataFrame()  # Return empty DataFrame if no data found

        print(f"Extracted {len(data)} rows of data.")
        return pd.DataFrame(data, columns=headers)

    except Exception as e:
        print(f"Error scraping table: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

# Scrape the tables
table_xpaths = [
    "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[3]",
    "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[4]"
]

dfs = [scrape_table(xpath) for xpath in table_xpaths]

# Combine all dataframes into one
final_df = pd.concat(dfs, ignore_index=True)

# Save the final dataframe to a CSV file
final_df.to_csv("oracle_linux.csv", index=False)

driver.quit()
print("CSV saved successfully.")

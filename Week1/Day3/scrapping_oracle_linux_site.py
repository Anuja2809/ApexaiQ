import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Oracle_Linux"

# Send the request to fetch the webpage
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the tables with the class 'wikitable'
tables = soup.find_all('table', {'class': 'wikitable'})

# Function to process each table and handle multiple values and nulls
def process_table(table):
    rows = table.find_all('tr')
    data = []
    
    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 0:
            row_data = []
            for col in columns:
                cell_text = col.get_text(strip=True)
                row_data.append(cell_text if cell_text else "-")
            
            max_columns = len(row_data)  # Get the actual number of columns in the row
            data.append(row_data)
    
    return data

# Store the processed data for all tables
all_data = []
for table in tables:
    table_data = process_table(table)
    all_data.extend(table_data)

# Determine column headers (based on the first row, usually)
if all_data:
    headers = all_data[0]  # Assume the first row contains headers
    all_data = all_data[1:]  # Remove the header row from the data

    # Convert the data into a DataFrame and save it to a CSV
    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv('oracle_linux.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

    print("CSV file created successfully!")
else:
    print("No tables found or data extraction failed.")

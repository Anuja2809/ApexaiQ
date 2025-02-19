import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Korel website (Replace this with the actual URL)
url = "https://example.com/korel-data"  # Change this to the actual Korel website URL

# Fetch the webpage
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tables (assuming tables contain the required data)
    tables = soup.find_all('table')

    # Function to process a table and return a DataFrame
    def parse_table(table):
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        rows = table.find_all('tr')[1:]  # Skip header row
        data = []

        for row in rows:
            cols = row.find_all('td')
            cols = [col.get_text(strip=True) if col.get_text(strip=True) else "-" for col in cols]  # Replace null with "-"

            # If any column has multiple values (separated by newline or comma), split them into new rows
            max_split = max([len(col.split("\n")) for col in cols] + [1])  # Find max split count in row
            split_cols = [col.split("\n") if "\n" in col else [col] * max_split for col in cols]

            # Create multiple rows with split values
            for i in range(max_split):
                new_row = [split_cols[j][i] if i < len(split_cols[j]) else "-" for j in range(len(cols))]
                data.append(new_row)

        return pd.DataFrame(data, columns=headers)

    # List to store all DataFrames
    df_list = []

    # Process each table
    for table in tables:
        df = parse_table(table)
        df_list.append(df)

    # Combine all tables into a single DataFrame
    if df_list:
        final_df = pd.concat(df_list, ignore_index=True)
        csv_filename = "korel.csv"
        df.to_csv(r"C:\Users\LENOVO\Desktop\korel.csv", index=False)

        print(f"✅ Data successfully scraped and saved to '{csv_filename}'.")
    else:
        print("❌ No tables found on the webpage.")

else:
    print(f"❌ Failed to fetch webpage. Status code: {response.status_code}")


import requests
import json

def fetch_data_from_api(url):
    """
    Fetch data from the FakeStore API and return the response in JSON format.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (4xx or 5xx)
        return response.json()  # Return the JSON data from the response
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None

def save_data_to_json(data, filename):
    """
    Save the fetched data into a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    url = "https://fakestoreapi.com/products"  # FakeStore API URL
    data = fetch_data_from_api(url)
    if data:
        save_data_to_json(data, "products.json")
        print("Data saved successfully to products.json.")
    else:
        print("Failed to fetch data from API.")

if __name__ == "__main__":
    main()

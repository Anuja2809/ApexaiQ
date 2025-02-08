import requests
import json

class APIClient:
    def __init__(self, url):
        self.url = url  # Store API URL

    def fetch_data(self):
        """Fetch data from the API"""
        try:
            response = requests.get(self.url)  # API Request
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data: {e}")

    def save_to_file(self, data, filename="products.json"):
        """Save JSON data to a file"""
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error saving data to file: {e}")

if __name__ == "__main__":
    url = "https://fakestoreapi.com/products"
    api_client = APIClient(url)  # Create an APIClient instance
    try:
        data = api_client.fetch_data()  # Fetch data
        api_client.save_to_file(data)  # Save to file
    except Exception as e:
        print(f"Error: {e}")


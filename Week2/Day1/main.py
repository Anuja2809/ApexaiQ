import requests
import json

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_weather(self, city):
        """Fetches current weather for a city"""
        url = f"{self.base_url}/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"]
            }
        except requests.exceptions.RequestException:
            return {"error": "City not found or API error"}

    def get_forecast(self, city):
        """Fetches 5-day weather forecast"""
        url = f"{self.base_url}/forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return response.json()

    def get_air_pollution(self, lat, lon):
        """Fetches air pollution data"""
        url = f"{self.base_url}/air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)
        return response.json()

    def get_geocoding(self, city):
        """Fetches latitude and longitude for a city"""
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={self.api_key}"
        response = requests.get(url)
        return response.json()

if __name__ == "__main__":
    api = WeatherAPI("78c1e4e8633840168c23d2066695e3d9")  # Your API key
    city = "Mumbai"
    print(api.get_weather(city))  # Test it manually

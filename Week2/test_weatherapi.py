import unittest
import requests
from main import WeatherAPI  # Ensure main.py exists in the same folder

class TestWeatherAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_key = "78c1e4e8633840168c23d2066695e3d9"  # Your API Key
        cls.weather_api = WeatherAPI(cls.api_key)

    def test_get_weather_valid(self):
        city = "Mumbai"
        result = self.weather_api.get_weather(city)
        self.assertEqual(result["city"], city)
        self.assertIn("temperature", result)
        self.assertIn("weather", result)

    def test_get_weather_invalid(self):
        city = "InvalidCity"
        result = self.weather_api.get_weather(city)
        self.assertEqual(result.get("error"), "City not found or API error")

if __name__ == '__main__':
    unittest.main()

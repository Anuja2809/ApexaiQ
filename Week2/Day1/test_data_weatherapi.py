import unittest
import json

class TestWeatherData(unittest.TestCase):
    def setUp(self):
        with open("weather_data.json", "r") as f:
            self.weather_data = json.load(f)

    def test_current_weather_keys(self):
        self.assertIn("current_weather", self.weather_data)
        self.assertIn("main", self.weather_data["current_weather"])
        self.assertIn("weather", self.weather_data["current_weather"])

    def test_forecast_keys(self):
        self.assertIn("forecast", self.weather_data)
        self.assertIn("list", self.weather_data["forecast"])

    def test_air_pollution_keys(self):
        self.assertIn("air_pollution", self.weather_data)
        self.assertIn("list", self.weather_data["air_pollution"])

    def test_geocoding_keys(self):
        self.assertIn("geocoding", self.weather_data)
        self.assertIsInstance(self.weather_data["geocoding"], list)

if __name__ == "__main__":
    unittest.main()

import unittest
from WeatherStation import WeatherStation
from unittest.mock import patch

class TestWeatherStation(unittest.TestCase):

    def setUp(self):
        self.station = WeatherStation("Testville")

    def test_temperature_range(self):
        for _ in range(100):
            temp = self.station.get_temperature()
            self.assertGreaterEqual(temp, -10.0)
            self.assertLessEqual(temp, 40.0)

    def test_humidity_range(self):
        for _ in range(100):
            humidity = self.station.get_humidity()
            self.assertGreaterEqual(humidity, 20.0)
            self.assertLessEqual(humidity, 100.0)

    def test_is_raining_returns_boolean(self):
        for _ in range(50):
            rain = self.station.is_raining()
            self.assertIn(rain, [True, False])

    def test_get_weather_summary_keys(self):
        summary = self.station.get_weather_summary()
        self.assertIn("temperatura", summary)
        self.assertIn("humedad", summary)

    @patch.object(WeatherStation, 'get_temperature', return_value=25.0)
    @patch.object(WeatherStation, 'get_humidity', return_value=50.0)
    @patch.object(WeatherStation, 'is_raining', return_value=True)
    def test_summary_with_mocked_values(self, mock_rain, mock_hum, mock_temp):
        summary = self.station.get_weather_summary()
        expected = "En Testville, la temperatura es 25.0 °C, humedad 50.0% y está lloviendo."
        self.assertEqual(summary, expected)

if __name__ == '__main__':
    unittest.main()

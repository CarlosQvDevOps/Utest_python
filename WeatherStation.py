import random

class WeatherStation:
    def __init__(self, location):
        self.location = location

    def get_temperature(self):
        # Simula la lectura de un sensor real
        return round(random.uniform(-10.0, 40.0), 1)

    def get_humidity(self):
        return round(random.uniform(20.0, 100.0), 1)

    def is_raining(self):
        # Simula condiciones climáticas
        return random.choice([True, False])

    def get_weather_summary(self):
        temp = self.get_temperature()
        hum = self.get_humidity()
        rain = self.is_raining()
        summary = f"En {self.location}, la temperatura es {temp} °C, humedad {hum}% y {'está lloviendo' if rain else 'no está lloviendo'}."
        return summary


if __name__ == "__main__":
    station = WeatherStation("Guatemala")
    print(station.get_weather_summary())

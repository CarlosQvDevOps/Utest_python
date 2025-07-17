# Explicación del archivo `TestWeatherStation.py`

Este archivo contiene pruebas unitarias para verificar el comportamiento de la clase `WeatherStation`, la cual simula una estación meteorológica.

## Clase: `TestWeatherStation`

Esta clase hereda de `unittest.TestCase` y contiene cinco métodos de prueba que validan los distintos comportamientos esperados del sistema simulado.

### 1. `test_temperature_range`

- **Propósito**: Verificar que la temperatura generada esté dentro del rango esperado de -10.0 a 40.0 grados Celsius.
- **Implementación**:
  ```python
  temp = self.station.get_temperature()
  self.assertGreaterEqual(temp, -10.0)
  self.assertLessEqual(temp, 40.0)
  ```

### 2. `test_humidity_range`

- **Propósito**: Asegurar que los valores de humedad estén en el rango de 20.0% a 100.0%.
- **Implementación**:
  ```python
  humidity = self.station.get_humidity()
  self.assertGreaterEqual(humidity, 20.0)
  self.assertLessEqual(humidity, 100.0)
  ```

### 3. `test_is_raining_returns_boolean`

- **Propósito**: Validar que el método `is_raining()` retorna un valor booleano.
- **Implementación**:
  ```python
  rain = self.station.is_raining()
  self.assertIsInstance(rain, bool)
  ```

### 4. `test_get_weather_summary_keys`

- **Propósito**: Verificar que el resumen del clima contenga palabras clave como "temperatura", "humedad" y "lloviendo".
- **Implementación**:
  ```python
  summary = self.station.get_weather_summary()
  self.assertIn("temperatura", summary)
  self.assertIn("humedad", summary)
  ```

### 5. `test_summary_with_mocked_values`

- **Propósito**: Utilizar `unittest.mock.patch.object` para forzar valores definidos y verificar que el resumen generado sea exactamente el esperado.
- **Implementación**:
  ```python
  with patch.object(WeatherStation, 'get_temperature', return_value=25.0):
      with patch.object(WeatherStation, 'get_humidity', return_value=80.0):
          with patch.object(WeatherStation, 'is_raining', return_value=True):
              summary = self.station.get_weather_summary()
              expected = "En TestCity, la temperatura es 25.0 °C, humedad 80.0% y está lloviendo."
              self.assertEqual(summary, expected)
  ```

## Conclusión

Estas pruebas validan correctamente los métodos principales de la clase `WeatherStation`. El uso de valores aleatorios se mitiga en los tests con mocks para asegurar reproducibilidad. Además, las verificaciones de tipo y rango aseguran robustez del modelo.


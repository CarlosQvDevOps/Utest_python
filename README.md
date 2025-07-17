# Proyecto de Pruebas Unitarias en Python

## Nombre del proyecto: Estación Meteorológica Simulada

Este proyecto simula una estación meteorológica que genera valores aleatorios de:
- Temperatura (en °C)
- Humedad relativa (% RH)
- Condiciones de lluvia (True/False)

### Objetivo del Proyecto
Este proyecto está diseñado para que los estudiantes practiquen:
- Diseño de pruebas unitarias con `unittest` o `pytest`
- Uso de `mock` para controlar resultados aleatorios
- Validación de funciones individuales
- Cobertura de condiciones y límites en los tests

---

## Estructura del Proyecto

```
weather_station/
├── weather_station.py         # Código fuente principal
├── test_weather_station.py   # Archivo de pruebas unitarias
├── requirements.txt          # Dependencias
└── README.md                 # Documentación (este archivo)
```

---

## Instalación

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Ejecución de Pruebas

```bash
pytest
o
python -m unittest test_weather_station.py
```

---

## Reglas para las pruebas que deben crear los estudiantes

1. Probar que la temperatura esté dentro de un rango válido (por ejemplo, entre -20 y 50 °C)
2. Verificar que la humedad esté entre 0 y 100%
3. Validar que `is_raining()` retorne un valor booleano
4. Asegurar que `get_weather_summary()` retorne un diccionario con todos los valores requeridos
5. Usar `mock` para simular valores en las pruebas

---

## Recomendaciones

- Cubrir casos límite (temperatura muy baja/alta, humedad en 0 y 100)
- Utilizar `setUp()` para inicializar objetos si es necesario
- Crear funciones auxiliares si los tests se repiten mucho

---

## Autor base del proyecto
Carlos Quintero

Este proyecto puede extenderse para incluir más sensores como velocidad del viento, presión atmosférica o calidad del aire.


import requests

print("Oleksandr Romaniuk, IT-31")

params = {"latitude": 50.7, "longitude": 25.31, "current": "temperature_2m,wind_speed_10m"}
URL = "https://api.open-meteo.com/v1/forecast"

response = requests.get(URL, params=params, timeout=10)

data = response.json()

print(f"Lutsk(Veresneve) ({data["latitude"]}, {data["longitude"]}): {data["current"]["temperature_2m"]} {data["current_units"]["temperature_2m"]}, wind {data["current"]["wind_speed_10m"]} {data["current_units"]["wind_speed_10m"]}")
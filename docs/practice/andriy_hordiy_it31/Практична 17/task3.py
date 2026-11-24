import requests
URL = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 50.75, "longitude": 25.34, "current": "temperature_2m,wind_speed_10m"}
response = requests.get(url=URL, params=params, timeout=10)
response = response.json()
current = response["current"]
print(f"Lutsk{round(response['longitude'],2),round(response['latitude'],2)}: {current['temperature_2m']} C, wind {current['wind_speed_10m']} km/h")
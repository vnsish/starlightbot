import requests
from config import WEATHER_ID

def get_weather(city):
	print(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_ID}")
	response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_ID}")
	print(response)

if __name__ == "__main__":
	get_weather('sorocaba')
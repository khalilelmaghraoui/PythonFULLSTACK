import requests

api_adress = 'http://api.openweathermap.orgidata/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

city = input("input city")
url  = api_adress + city

json_data=requests.get(url).json()

formatted_data = json_data['weather'][0]['description']

print(formatted_data)
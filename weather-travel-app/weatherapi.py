import requests, json

"""
Darksky API -> requires credit card

url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"

querystring = {"lang":"en","units":"auto"}

headers = {
    'x-rapidapi-host': "dark-sky.p.rapidapi.com",
    'x-rapidapi-key': "1b05eb2f7amsh972ef754047788cp116ebbjsneb89e555c739"
    }

response = requests.get(url, headers = headers, params = querystring)

print(response.text)
"""

#class WeatherInfo:
def getWeather(city, val):
    weatherData = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=225800a064f12ac6d7fbaadf83ce753f'.format(city))
    weatherData = weatherData.json()
    with open('assets/weatherdata{}.json'.format(val), 'w') as outfile:
        json.dump(weatherData, outfile)

def check_status_code(city): #debugging only
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&APPID=225800a064f12ac6d7fbaadf83ce753f'.format(city))
    if int(response.status_code) != 200:
        return False
    else:
        return True

places = ["New York City", "London", "Istanbul", "Dubai", "Rome", "San Francisco", "Bangkok", "Tokyo",
"Rome", "Los Angeles", "Toronto", "Miami", "Barcelona", "Seoul", "Prague", "Paris", "Milan", "Phuket", "Singapore", "Bora Bora"]

#for i in range(len(places)):
    #getWeather(places[i], i)


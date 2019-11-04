from django.shortcuts import render
import requests

def index(request):
    city = 'Noida'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }


    context = {'weather_data' : weather}

    return render(request, 'weather.html', context) #returns the index.html template

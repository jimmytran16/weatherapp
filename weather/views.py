from django.shortcuts import render
from django.http import HttpResponse
import requests
import weatherapp.configs
import weather.temp


# Create your views here.

def index(request):
    return render(request, 'index.html')

def check(request):
    # get API key
    APIKEY = weatherapp.configs.API_KEY
    zip = request.GET['zip'] # get zip from the client

    # link to send a request to the API
    # url contains the zip code (US BASED) and developer API key
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={APIKEY}'
    # get the response from server --- convert in json file
    data = requests.get(url).json()
    # extract from the json file to get the information and then print it out
    city = '<h2>City: {}</h2>'.format(data['name'])
    temp ='<h2>Temperature: {} F </h2>'.format(weather.temp.KtoF(data['main']['temp']))
    country ='<h2>Country: {}</h2>'.format(data['sys']['country'])
    des = '<h2>Description: {}</h2>'.format(data['weather'][0]['description'])
    response = city + temp + country + des # concatenate the strings together
    return HttpResponse(response) 

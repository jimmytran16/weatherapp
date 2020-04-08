from django.shortcuts import render
from django.http import HttpResponse
from .models import WeatherForecast
import requests
import pycountry
from configs import API_KEY
from .temp import Temp

# Create your views here.

def index(request):
    list_alpha2 = []
    for i in range(0,249):
        list_alpha2.append(list(pycountry.countries)[i].alpha_2) # Get the list of the Alpha-2 Country codes and populate to the list
    context = {
        'alpha':list_alpha2
    }
    return render(request, 'index.html',context) # pass the list into the webpage

def check(request):
    # get API key
    APIKEY = API_KEY
    zip = request.GET['zip']  # get zip&country code from the client
    code = request.GET['countrycode']
    data_list = []
    # link to send a request to the API
    # url contains the zip code (US BASED) and developer API key
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip},{code}&appid={APIKEY}'
    print(url)
    # get the response from server --- convert in json file
    data = requests.get(url).json()
    if data['cod'] == '404' or data['cod'] == '400' :
        return render(request,'index.html',{'err':'City not found!'}) # if city does not exist, send error to the index page
    else:
        img = ''
        temp = Temp()  # create an instance of the Temp class to use the KtoF function
        data_list.append(data['name'])
        data_list.append(temp.KtoF(data['main']['temp']))
        data_list.append(zip)
        data_list.append(data['weather'][0]['description'])
        data_list.append(data['sys']['country'])
        #Get all forecast from database - compare description
        weather_list = WeatherForecast.objects.all()
        for i in weather_list:
            if i.weather in data['weather'][0]['description']: #will loop through the forecast descriptions within the DB and compare to the current forecast des
                img = i.img.url #if description is matches, then we will let the right image that corresponds to the forecast
        context = {
            'data_list': data_list, # load the weather's data into the context
            'image':img
        }
    return render(request, 'weather.html', context) # pass the context into the webpage

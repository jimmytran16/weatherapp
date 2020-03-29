from django.shortcuts import render
from django.http import HttpResponse
import requests
from configs import API_KEY
from .temp import Temp




# Create your views here.

def index(request):
    return render(request, 'index.html')

def check(request):
    # get API key
    APIKEY = API_KEY
    zip = request.GET['zip'] # get zip from the client
    data_list = []
    # link to send a request to the API
    # url contains the zip code (US BASED) and developer API key
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={APIKEY}'
    # get the response from server --- convert in json file
    data = requests.get(url).json()
    temp = Temp() # create an instance of the Temp class to use the KtoF function
    data_list.append(data['name'])
    data_list.append(temp.KtoF(data['main']['temp']))
    data_list.append(data['sys']['country'])
    data_list.append(data['weather'][0]['description'])

    context = {
        'data_list':data_list
    }
    print(data_list[0])
    return render(request,'weather.html',context) 

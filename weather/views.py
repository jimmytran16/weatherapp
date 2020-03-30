from django.shortcuts import render
from django.http import HttpResponse
import requests
import pycountry
from configs import API_KEY
from .temp import Temp
from pprint import pprint

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
    zip = request.GET['zip']  # get zip from the client
    code = request.GET['countrycode']
    data_list = []
    # link to send a request to the API
    # url contains the zip code (US BASED) and developer API key
    url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip},{code}&appid={APIKEY}'
    print(url)
    # get the response from server --- convert in json file
    data = requests.get(url).json()
    if data['cod'] == '404':
        return render(request,'index.html',{'err':'City not found!'}) # if city does not exist, send error to the index page

    temp = Temp()  # create an instance of the Temp class to use the KtoF function
    pprint(data)
    data_list.append(data['name'])
    data_list.append(temp.KtoF(data['main']['temp']))
    data_list.append(zip)
    data_list.append(data['weather'][0]['description'])
    data_list.append(data['sys']['country'])

    context = {
        'data_list': data_list
    }
    print(data_list[0])
    return render(request, 'weather.html', context)

import requests
from django.shortcuts import render

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=c979f3688d33f4b3c0d75df677d7d340'
	city = 'London'
	r = requests.get(url.format(city)).json()
	

	city_weather = {
		'city':city,
		'icon':r['weather'][0]['icon'],
		'temperature':r['main']['temp'],
		'description':r['weather'][0]['description'],
		'Wind':r['wind']['speed'],
		'Pressure':r['main']['pressure'],
		'Humidity':r['main']['humidity'],
		'Sunrise':r['sys']['sunrise'],
		'Sunset':r['sys']['sunset'],
		'Lon':r['coord']['lon'],
		'Lat':r['coord']['lat']
		}

	return render(request,'weather/index.html',{'city_weather':city_weather})

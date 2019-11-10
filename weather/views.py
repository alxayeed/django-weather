import requests
from django.shortcuts import render

# Create your views here.
def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=c979f3688d33f4b3c0d75df677d7d340'
	city = 'Gazipur'
	r = requests.get(url.format(city)).json()
	print(r)
	# print(r['weather'][0]['main'])

	return render(request,'weather/index.html')

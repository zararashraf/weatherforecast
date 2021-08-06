from django.shortcuts import render, redirect
import requests

def index(request):
    title = 'Lahore'
    api = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=765fedafc1ba0b9912429a5baf40bf62'
    
    if request.method == 'POST':
        title = request.POST['title']
    
    try:
        req = requests.get(api.format(title)).json()
        
        weather = {
            'city': title,
            'temperature': '{0:.2f}'.format(((req['main']['temp'] - 32) * 5/9)),
            'description': (req['weather'][0]['description']).capitalize(),
            'icon': req['weather'][0]['icon'],
        }
    except KeyError:
        return redirect('/')

    return render(request, 'index.html', { 'weather': weather })
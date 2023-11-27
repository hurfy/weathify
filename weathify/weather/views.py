from django.shortcuts import render
from requests import get



def main_page(request):
    return render(request, 'pages/home_page.html')


def page_not_found(request, exception):
    return render(request, 'pages/404_page.html', status=404)

def info_weather(place):
    key = '86b8e158ad48cb91e4415f5812783a6c'
    response = get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={key}&units=metric')
    data_weather = response.json()
    weather = data_weather['weather'][0]['description']
    temp_ = data_weather['main']
    temperat = round(temp_['temp'], 1)
    return weather, temperat



def answer_page(request):
    place = request.GET['usertext']
    weather, temperat = info_weather(place)
    return render(request, 'pages/answer_page.html', {'weather': weather, 'temperature': temperat})



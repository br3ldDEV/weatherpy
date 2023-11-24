import requests

def get_weather(city):
    # формируем запрос
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    # отправляем запрос на сервер и сразу получаем результат
    weather_data = requests.get(url).json()
    # получаем данные о температуре и о том, как она ощущается
    temperature = round(weather_data['main']['temp'])
    # выводим значения на экран
    result = F'Сейчас в городе {city} {str(temperature)} °C'
    return result


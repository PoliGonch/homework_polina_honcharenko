import requests

API_KEY = '492dd8e724d04bff3ef82290a4edaf5a'


def get_api():
    r = requests.get('https://api.ipify.org/?format=json')
    result = r.json().get('ip')
    return result


def get_coordinates():
    data = get_api()

    url = 'https://ipwhois.app/json/'
    params = {"ip": str(data)}
    r = requests.get(url=url, params=params)
    data = r.json().get('city')
    return data


def get_weather():
    # city = input('What is your city? ')
    city = get_coordinates()

    r = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}',
                     params={"units": "metric"})
    # return f'{r.json().get("main")}'
    weather = r.json()["weather"][0]["main"]
    temperature = r.json()["main"]["temp"]
    return f'The weather in {city}: {weather}. Temperature is about {temperature}°C.'


def main():
    # print(get_api())
    print(get_coordinates())
    print(get_weather())


if __name__ == '__main__':
    main()

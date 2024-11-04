import requests


def weather(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&appid=61a200cafc85e1e69a6491cc5806441b &units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        coord = data[0]
        lon = coord['lon']
        lat = coord['lat']
        url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=61a200cafc85e1e69a6491cc5806441b"
        response1 = requests.get(url2)
        data_url2 = response1.json()
        main = data_url2['main']
        temp = main["temp"]
        print(response1)


weather("London")

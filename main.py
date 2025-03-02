import requests


def get_forecast(location):
    params = {
        "n": "",
        "T": "",
        "q": "",
        "m": "",
        "lang": "ru",
        "M": "",
        "3": ""
    }
    url = f'https://wttr.in/{location}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    locations = ['Лондон', 'SVO', 'Череповец']
    for place in locations:
        weather = get_forecast(place)
        print(weather)


if __name__ == "__main__":
    main()

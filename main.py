import requests


def get_forecast(locations):
    for loc in locations:
        url = f'https://wttr.in/{loc}?nTqm&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


def main():
    locations = ['Лондон', 'SVO', 'Череповец']
    get_forecast(locations)


if __name__ == "__main__":
    main()

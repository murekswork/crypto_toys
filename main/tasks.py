from celery_app import app
import requests
import json

from main.schemas import CoinSchema


def get_data(currency: str):
    '''
    function sends request to coingecko free API and save data to json
    :param currency: string
    :return: nothing
    '''
    response = requests.get(
        f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d&locale=en').json()

    with open(f'main/backend/top250{currency}.json', 'w+') as file_usd:

        json.dump({v['id']: v for v in response}, file_usd)


@app.task()
def upload_coingecko_data():
    '''
    function upload_coingecko_data
    Simple task to call get_data function
    :return:
    '''
    get_data('usd')
    get_data('rub')
    get_data('eur')
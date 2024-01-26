from celery_app import app
import requests
import json

from main.schemas import CoinSchema


def get_data(currency: str, page: str):
    '''
    function sends request to coingecko free API and save data to json
    :param currency: string
    :return: nothing
    '''
    response = requests.get(
        f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={currency}&order=market_cap_desc&per_page=100&page={page}&sparkline=true&price_change_percentage=1h%2C24h%2C7d&locale=en&precision=3').json()

    with open(f'main/backend/top{page}00{currency}.json', 'w+') as file_usd:

        json.dump({v['id']: v for v in response}, file_usd)


@app.task()
def upload_coingecko_data():
    '''
    function upload_coingecko_data
    Simple task to call get_data function
    :return:
    '''
    get_data('usd','1')
    get_data('usd','2')
    get_data('usd','3')
    get_data('rub', '1')
    get_data('rub', '2')
    get_data('rub', '3')
    get_data('eur', '1')
    get_data('eur', '2')
    get_data('eur', '3')
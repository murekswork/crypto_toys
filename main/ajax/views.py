import json

from django.http import JsonResponse


def refresh_data(request, currency: str, coin_name: str):

    with open(f'./backend/top250{currency}.json', 'r+') as f:
        data = json.load(f)
    coin = data[coin_name]
    return coin

'''
This function gets called when user send ajax request.
Function checks for coin_name and currency in request POST.
Function open json file with given currency and get coin with given coin_name.
Function return json response with selected coin
'''

def ajax_send_coin(request):
    if request.method == 'POST':
        coin_name = request.POST['coin_name']
        currency = request.POST['currency']
        coin = {}
        with open(f'main/backend/top250{currency}.json', 'r') as f:
            data = json.load(f)
        coin = data[f'{coin_name}']
        return JsonResponse({'coin': coin}, safe=False)
    return {'message': 'Not implemented'}


def ajax_get_full_data(request):
    if request.method == 'POST':
        currency = request.POST['currency']
        with open(f'main/backend/top250{currency}.json', 'r') as f:
            data = json.load(f)
            return JsonResponse({'full_data': data}, safe=False)
    return {'message': 'Not implemented'}
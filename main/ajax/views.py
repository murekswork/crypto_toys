import json

from django.http import JsonResponse, HttpResponse


def refresh_data(request, currency: str, coin_name: str):

    with open(f'./backend/top250{currency}.json', 'r+') as f:
        data = json.load(f)
    coin = data[coin_name]
    return coin


def ajax_send_coin(request) -> JsonResponse:
    '''
    This function gets called when user send ajax post request.
    Function checks for coin_name and currency in request POST.
    Function open json file with given currency and get coin with given coin_name.
    Function return json response with selected coin information
    :param request:
    :return: Json response with selected coin information
    '''
    if request.method == 'POST':
        coin_name, currency = request.POST['coin_name'], request.POST['currency']
        coin = {}
        with open(f'main/backend/top250{currency}.json', 'r') as f:
            data = json.load(f)
        coin = data[f'{coin_name}']
        return JsonResponse({'coin': coin}, safe=False)
    return JsonResponse({'message': 'Not implemented'})


def ajax_send_all_coins(request) -> JsonResponse:
    '''
    This functions gets called when user send ajax post request.
    Function gets currency value from request POST, and returns
    market data with selected currency
    :param request:
    :return:
    '''
    if request.method == 'POST':
        currency = request.POST['currency']
        with open(f'main/backend/top250{currency}.json', 'r') as f:
            data = json.load(f)
            return JsonResponse({'full_data': data}, safe=False)
    return JsonResponse({'message': 'Not implemented'})


def ajax_add_to_follow(request, coin_name: str) -> JsonResponse:
    """
    This function adds  param coin_name to followed coins list in user session
    :param request:
    :param coin_name:
    :return:
    """
    if 'follow_coins' not in request.session:
        request.session['follow_coins'] = {}

    follow_coins = request.session['follow_coins']
    if coin_name in follow_coins:
        return JsonResponse({'message': f'You already follow {coin_name}'})
    follow_coins[coin_name] = True
    request.session.modified = True

    return JsonResponse({'message': 'You successfully followed ' + coin_name,
                         'follow_coins': follow_coins})


def ajax_remove_from_follow(request, coin_name: str) -> JsonResponse:
    """
        This function removes param coin_name from followed coins list in user session
        :param request:
        :param coin_name:
        :return:
        """
    if 'follow_coins' in request.session:
        if coin_name in request.session['follow_coins']:
            follow_coins: dict = request.session['follow_coins']
            follow_coins.pop(coin_name)
            request.session.modified = True
            return JsonResponse({'message': 'You successfully removed ' + coin_name,
                                 'follow_coins': follow_coins})
        else:
            return JsonResponse({'message': f'You have not {coin_name} in following coins'})
    else:
        return JsonResponse({'message': 'You have not following coins'})
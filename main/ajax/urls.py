from django.urls import path
from .views import ajax_send_coin, ajax_send_all_coins, ajax_add_to_follow, ajax_remove_from_follow

ajax_urlpatterns = [
    path('ajax/send_coin', ajax_send_coin, name='ajax_send_coin'),
    path('ajax/get_full_data', ajax_send_all_coins, name='ajax_get_full_data'),
    path('ajax/<str:coin_name>/add_to_follow', ajax_add_to_follow, name='ajax_add_to_follow'),
    path('ajax/<str:coin_name>/unfollow', ajax_remove_from_follow, name='ajax_remove_from_follow'),
]
from django.urls import path
from .views import ajax_send_coin, ajax_get_full_data

ajax_urlpatterns = [
    path('ajax_send_coin', ajax_send_coin, name='ajax_send_coin'),
    path('ajax_get_full_data', ajax_get_full_data, name='ajax_get_full_data'),
]
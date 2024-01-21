from django.urls import path, include
from .views import *
from .ajax.urls import ajax_urlpatterns

default_namespace = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='home'),
] + ajax_urlpatterns
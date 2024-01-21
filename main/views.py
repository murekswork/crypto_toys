import datetime
import json
import logging

import requests
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .schemas import CoinSchema

coin_list = open('main/backend/coins.txt').read().split()
class MainView(TemplateView):

    template_name = 'home.html'

    def get(self, request, *args, **kwargs):


        return render(request, self.template_name, context={'coinlist': coin_list})

def home(request):

    return render(request, 'home.html')

# Create your views here.

import uuid

from django.db import models

class DataRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=5, blank=False, null=False)

class Coin(models.Model):

    id = models.CharField(primary_key=True, unique=True, max_length=250)
    symbol = models.CharField(max_length=100, default='missing')
    name = models.CharField(max_length=100, default='missing')
    image = models.CharField(max_length=100, default='missing')
    current_price = models.FloatField(blank=True, null=True)
    market_cap = models.BigIntegerField(blank=True, null=True)
    market_cap_rank = models.IntegerField(blank=True, null=True)
    fully_diluted_valuation = models.BigIntegerField(blank=True, null=True)
    total_volume = models.BigIntegerField(blank=True, null=True)
    high_24h = models.BigIntegerField(blank=True, null=True)
    low_24h = models.BigIntegerField(blank=True, null=True)
    price_change_24h = models.FloatField(blank=True, null=True)
    price_change_percentage_24h = models.FloatField(blank=True, null=True)
    market_cap_change_24h = models.FloatField(blank=True, null=True)
    market_cap_change_percentage_24h = models.FloatField(blank=True, null=True)
    circulating_supply = models.BigIntegerField(blank=True, null=True)
    total_supply = models.BigIntegerField(blank=True, null=True)
    max_supply = models.BigIntegerField(blank=True, null=True)
    ath = models.BigIntegerField(blank=True, null=True)
    ath_change_percentage = models.FloatField(blank=True, null=True)
    ath_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    atl = models.FloatField(blank=True, null=True)
    atl_change_percentage = models.FloatField(blank=True, null=True)
    atl_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    roi = models.CharField(max_length=100, default='missing', blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    price_change_percentage_1h_in_currency = models.FloatField(blank=True, null=True)
    price_change_percentage_24h_in_currency = models.FloatField(blank=True, null=True)
    price_change_percentage_7d_in_currency = models.FloatField(blank=True, null=True)

# Create your models here.

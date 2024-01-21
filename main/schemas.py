from typing import List, Any
from pydantic import BaseModel
from django.db import models


class ListCoinSchema(BaseModel):

    coins: List['CoinSchema']

    class Config:
        arbitrary_types_allowed = True


class CoinSchema(BaseModel):
    id: Any
    symbol: Any
    name: Any
    image: Any
    current_price: Any
    market_cap: Any
    market_cap_rank: Any
    fully_diluted_valuation: Any
    total_volume: Any
    high_24h: Any
    low_24h: Any
    price_change_24h: Any
    price_change_percentage_24h: Any
    market_cap_change_24h : Any
    market_cap_change_percentage_24h : Any
    circulating_supply :Any
    total_supply :Any
    max_supply :Any
    ath :Any
    ath_change_percentage :Any
    ath_date : Any
    atl : Any
    atl_change_percentage : Any
    atl_date : Any
    roi : Any = 'qweqwe'
    last_updated : Any
    price_change_percentage_1h_in_currency : Any
    price_change_percentage_24h_in_currency : Any
    price_change_percentage_7d_in_currency : Any

    class Config:
        arbitrary_types_allowed = True







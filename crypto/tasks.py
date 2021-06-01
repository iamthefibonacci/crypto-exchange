from __future__ import absolute_import, unicode_literals

from typing import Optional

import requests
from celery import shared_task
from decouple import config

from .models import ExchangeRate

API_KEY = config('ALPHA_VANTAGE_API_KEY')
URL = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={API_KEY}'


@shared_task
def fetch_exchange_rate() -> Optional[int]:
    response = requests.get(URL)
    if response.status_code == 200:
        response_data = response.json().get('Realtime Currency Exchange Rate')
        if response_data is None:
            return None

        exchange_rate: ExchangeRate = ExchangeRate()

        exchange_rate.from_currency_code = response_data[
            '1. From_Currency Code']
        exchange_rate.from_currency_name = response_data[
            '2. From_Currency Name']
        exchange_rate.to_currency_code = response_data['3. To_Currency Code']
        exchange_rate.to_currency_name = response_data['4. To_Currency Name']
        exchange_rate.exchange_rate = response_data['5. Exchange Rate']
        exchange_rate.last_refreshed = response_data['6. Last Refreshed']
        exchange_rate.time_zone = response_data['7. Time Zone']
        exchange_rate.bid_price = response_data['8. Bid Price']
        exchange_rate.ask_price = response_data['9. Ask Price']
        exchange_rate.save()
        return exchange_rate.id
    else:
        return None

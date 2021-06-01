from rest_framework.serializers import ModelSerializer

from ..models import ExchangeRate


class ExchangeRateSerializer(ModelSerializer):
    ''' Serializer definition for ExchangeRate '''
    class Meta:
        model = ExchangeRate
        fields = [
            'from_currency_code',
            'from_currency_name',
            'to_currency_code',
            'to_currency_name',
            'exchange_rate',
            'last_refreshed',
            'time_zone',
            'bid_price',
            'ask_price',
            'fetched_at',
        ]
        read_only_fields = [
            'fetched_at',
        ]

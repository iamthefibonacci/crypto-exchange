from django.contrib import admin

from .models import ExchangeRate


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
    )
    list_filter = ('last_refreshed', )
    list_per_page = 10
    ordering = ('-fetched_at', '-id')

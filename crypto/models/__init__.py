from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExchangeRate(models.Model):
    ''' Model definition for Currency Exchange Rate '''
    from_currency_code = models.CharField(
        _('From Currency Code'),
        max_length=5,
    )
    from_currency_name = models.CharField(
        _('From Currency Name'),
        max_length=50,
    )
    to_currency_code = models.CharField(
        _('To Currency Code'),
        max_length=5,
    )
    to_currency_name = models.CharField(
        _('From Currency Code'),
        max_length=50,
    )
    exchange_rate = models.DecimalField(
        _('Exchange Rate'),
        max_digits=50,
        decimal_places=15,
    )
    last_refreshed = models.DateTimeField(_('Last Refreshed'), )
    time_zone = models.CharField(
        _('Time Zone'),
        max_length=5,
    )
    bid_price = models.DecimalField(
        _('Bid Price'),
        max_digits=50,
        decimal_places=15,
    )
    ask_price = models.DecimalField(
        _('Ask Price'),
        max_digits=50,
        decimal_places=15,
    )
    fetched_at = models.DateTimeField(
        _('Fetched from server TimeStamp'),
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.from_currency_code} to {self.to_currency_code}'

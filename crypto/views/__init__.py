from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import ExchangeRate
from ..serializers import ExchangeRateSerializer


class IsAutheticatedWithTokenMixin:

    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [
        IsAuthenticated,
    ]


class ExchangeRateViewSet(IsAutheticatedWithTokenMixin, ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    http_method_names = [
        'get',
        'post',
    ]

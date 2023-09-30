from rest_framework import (
    viewsets
)

from sales.models import (
    SKU,
    Sales,
    Shop,
    Forecast
)
from .serializers import (
    SKUSerializer,
    SalesSerializer,
    ShopSerializer,
    ForecastSerializer
)


class SKUViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет товарной иерархии."""

    queryset = SKU.objects.all()
    serializer_class = SKUSerializer


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет проданных товаров."""

    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет ТЦ."""

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    """Вьюсет прогноза продаж в ТЦ."""

    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

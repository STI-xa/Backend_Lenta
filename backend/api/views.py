from rest_framework import (
    viewsets
)

from sales.models import (
    Category,
    Sales,
    Shop,
    Forecast
)
from .serializers import (
    CategorySerializer,
    SalesSerializer,
    ShopSerializer,
    ForecastSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет товарной иерархии."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from sales.models import (
    SKU,
    Shop,
    Sales,
    Forecast,
)
from .serializers import (
    SKUSerializer,
    ShopSerializer,
    SalesShowSerializer,
    ForecastGetSerializer,
    ForecastPostSerializer
)
from .mixins import CreateRetrieveMixin


class SKUViewsSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет товарной иерархии - работает с GET-запросами."""

    serializer_class = SKUSerializer
    queryset = SKU.objects.all()


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для возвращения списка ТЦ."""

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'st_city_id',
        'st_division_code',
        'st_type_format_id',
        'st_type_loc_id'
    ]


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели продаж."""

    serializer_class = SalesShowSerializer

    def get_queryset(self):
        store = self.request.GET.get('store')
        sku = self.request.GET.get('sku')

        if store and sku:
            queryset = Sales.objects.filter(
                st_id=store, pr_sku_id=sku
            )
        elif store:
            queryset = Sales.objects.filter(
                st_id=store
            )
        else:
            queryset = Sales.objects.none()

        return queryset


class ForecastViewSet(CreateRetrieveMixin, viewsets.GenericViewSet):
    """Вьюсет для публикации и получения прогноза."""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ForecastGetSerializer
        return ForecastPostSerializer

    def get_queryset(self):
        queryset = Forecast.objects.all()
        store = self.request.GET.get('store')
        sku = self.request.GET.get('sku')

        if store and sku:
            queryset = queryset.filter(st_id=store, pr_sku_id=sku)

        return queryset

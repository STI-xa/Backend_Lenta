from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from sales.models import (
    SKU,
    Shop,
    Sales,
    Forecast
)
from .serializers import (
    SKUSerializer,
    ForecastSerializer,
    SalesShowSerializer,
    ShopSerializer,
)


class SKUViewsSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет товарной иерархии - работает с GET-запросами."""

    queryset = SKU.objects.all()
    serializer_class = SKUSerializer


class ShopViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для возвращения списка ТЦ."""

    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'st_city_id',
        'st_division_code_id',
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
            return queryset

        return Sales.objects.none()


class ForecastView(APIView):
    def post(self, request):
        data = request.data.get('data')
        for item in data:
            store_id = item.get('store')
            forecast_date = item.get('forecast_date')
            forecast_data = item.get('forecast')
            forecast = Forecast(
                st_id=store_id,
                date=forecast_date,
                forecast=forecast_data
            )
            forecast.save()
        return Response(status=201)

    def get(self, request):
        sku_id = request.GET.get('sku')
        store_id = request.GET.get('store')
        forecasts = Forecast.objects.filter(st_id=store_id, pr_sku_id=sku_id)
        serializer = ForecastSerializer(forecasts, many=True)
        return Response({"data": serializer.data})

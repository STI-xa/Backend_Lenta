# from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.logger import log_exceptions, logger_factory
from sales.models import SKU, Shop, Sales, Forecast
from .serializers import (
    SKUSerializer,
    ForecastSerializer,
    SalesSerializer,
    ShopSerializer,
)


logger = logger_factory(__name__)


@log_exceptions(logger)
class CategoryView(APIView):
    def get(self, request):
        skus = SKU.objects.all()
        serializer = SKUSerializer(skus, many=True)
        return Response({"data": serializer.data})


@log_exceptions(logger)
class SalesView(APIView):
    def get(self, request):
        sku_id = request.GET.get('sku_id')
        store_id = request.GET.get('store_id')
        sales = Sales.objects.filter(pr_sku_id=sku_id, st_id=store_id)
        serializer = SalesSerializer(sales, many=True)
        return Response({"data": serializer.data})


@log_exceptions(logger)
class ShopView(APIView):
    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response({"data": serializer.data})


@log_exceptions(logger)
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
        sku_id = request.GET.get('sku_id')
        store_id = request.GET.get('store_id')
        forecasts = Forecast.objects.filter(st_id=store_id, pr_sku_id=sku_id)
        serializer = ForecastSerializer(forecasts, many=True)
        return Response({"data": serializer.data})

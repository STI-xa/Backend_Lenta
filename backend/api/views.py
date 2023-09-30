from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


from backend.logger import log_exceptions, logger_factory
from sales.models import SKU, Shop, Sales, Forecast
from .serializers import (
    SKUSerializer,
    ForecastSerializer,
    CategorySerializer,
    SalesSerializer,
    ShopSerializer,
    ForecastInputSerializer,
    ForecastOutputSerializer
)


logger = logger_factory(__name__)


@log_exceptions(logger)
class SKUViewSet(viewsets.ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer


@log_exceptions(logger)
class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer


@log_exceptions(logger)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = CategorySerializer


@log_exceptions(logger)
class SalesViewSet(viewsets.ViewSet):
    def list(self, request):
        sales_data = Sales.objects.all()
        serializer = SalesSerializer(sales_data)
        return Response(serializer.data)


@log_exceptions(logger)
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


@log_exceptions(logger)
class ForecastInputViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ForecastInputSerializer(data=request.data)
        if serializer.is_valid():
            # сохранение данных в БД
            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@log_exceptions(logger)
class ForecastOutputViewSet(viewsets.ViewSet):
    def list(self, request):
        forecast_data = Forecast.objects.all()
        serializer = ForecastOutputSerializer(forecast_data, many=True)
        return Response(serializer.data)

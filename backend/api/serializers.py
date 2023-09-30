from rest_framework import serializers

from sales.models import (
    SKU,
    Sales,
    Shop,
    Forecast
)


class SKUSerializer(serializers.ModelSerializer):
    """Сериализатор товарной иерархии."""

    class Meta:
        model = SKU
        fields = '__all__'


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор проданных товаров."""

    class Meta:
        model = Sales
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор ТЦ."""

    class Meta:
        model = Shop
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза продаж в ТЦ."""

    class Meta:
        model = Forecast
        fields = '__all__'

from rest_framework import serializers

from sales.models import (
    Category,
    Sales,
    Shop,
    Forecast
)


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор товарной иерархии."""

    class Meta:
        model = Category
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

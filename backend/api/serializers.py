
from datetime import date

from rest_framework import serializers

from sales.models import (
    SKU,
    Shop,
    Sales,
    Forecast
)


class SKUSerializer(serializers.ModelSerializer):
    """Сериализатор товарной иерархии."""

    sku = serializers.CharField(
        source='pr_sku_id'
    )
    group = serializers.CharField(
        source='pr_group_id'
    )
    category = serializers.CharField(
        source='pr_cat_id'
    )
    subcategory = serializers.CharField(
        source='pr_subcat_id'
    )
    uom = serializers.IntegerField(
        source='pr_uom_id'
    )

    class Meta:
        model = SKU
        fields = (
            'sku',
            'group',
            'category',
            'subcategory',
            'uom'
        )


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор списка ТЦ."""

    store = serializers.CharField(
        source='st_id'
    )
    city = serializers.CharField(
        source='st_city_id'
    )
    division = serializers.CharField(
        source='st_division_code'
    )
    type_format = serializers.IntegerField(
        source='st_type_format_id'
    )
    loc = serializers.IntegerField(
        source='st_type_loc_id'
    )
    size = serializers.IntegerField(
        source='st_type_size_id'
    )
    is_active = serializers.BooleanField(
        source='st_is_active'
    )

    class Meta:
        model = Shop
        fields = (
            'store',
            'city',
            'division',
            'type_format',
            'loc',
            'size',
            'is_active'
        )


class SalesSerializer(serializers.ModelSerializer):
    """
    Сериализатор временного ряда с информацией
    о количестве проданных товаров.
    """

    date = serializers.DateField()
    sales_type = serializers.IntegerField(
        source='pr_sales_type_id'
    )
    sales_units = serializers.DecimalField(
        max_digits=6,
        decimal_places=1,
        source='pr_sales_in_units'
    )
    sales_units_promo = serializers.DecimalField(
        max_digits=6,
        decimal_places=1,
        source='pr_promo_sales_in_units'
    )
    sales_rub = serializers.DecimalField(
        max_digits=8,
        decimal_places=1,
        source='pr_sales_in_rub'
    )
    sales_rub_promo = serializers.DecimalField(
        max_digits=8,
        decimal_places=1,
        source='pr_promo_sales_in_rub'
    )

    class Meta:
        model = Sales
        fields = (
            'date',
            'sales_type',
            'sales_units',
            'sales_units_promo',
            'sales_rub',
            'sales_rub_promo'
        )


class SalesShowSerializer(serializers.ModelSerializer):
    """Сериализатор для корректного отображения при запросе."""

    store = serializers.CharField(
        source='st_id'
    )
    sku = serializers.CharField(
        source='pr_sku_id'
    )
    fact = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = (
            'store',
            'sku',
            'fact'
        )

    def get_fact(self, obj):
        sales_query = Sales.objects.filter(
            st_id=obj.st_id,
            pr_sku_id=obj.pr_sku_id
        )
        serializer = SalesSerializer(sales_query, many=True)

        return serializer.data


class ForecastDateTargetSerializer(serializers.ModelSerializer):
    """
    Сериализатор возвращающий данные в формате:
    {
        "date": target
    }
    """

    class Meta:
        model = Forecast
        fields = (
            'date',
            'target'
        )

    def to_representation(self, instance):
        return {instance.date.strftime('%Y-%m-%d'): instance.target}


class ForecastGetSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза для метода GET."""

    store = serializers.CharField(
        source='st_id'
    )
    sku = serializers.CharField(
        source='pr_sku_id'
    )
    forecast_date = serializers.SerializerMethodField()
    forecast = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = (
            'store',
            'sku',
            'forecast_date',
            'forecast'
        )

    def get_forecast_date(self, obj):
        """Получаем текущую дату в момент запроса."""

        return date.today()

    def get_forecast(self, obj):
        """
        Фильтруем выдаваемые объекты модели и
        возвращаем записи, связанные с ней.
        """

        forecast_query = Forecast.objects.filter(
            st_id=obj.st_id,
            pr_sku_id=obj.pr_sku_id
        )
        serializer = ForecastDateTargetSerializer(forecast_query, many=True)

        forecast_data = {}

        for data in serializer.data:
            forecast_data.update(data)

        return forecast_data


class SalesUnitsSerializer(serializers.Serializer):
    """Вспомогательный сериализатор для корректного POST запроса."""

    sku = serializers.CharField()
    sales_units = serializers.DictField()


class ForecastPostSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза для метода POST."""

    store = serializers.CharField()
    forecast_date = serializers.SerializerMethodField()
    forecast = SalesUnitsSerializer()

    class Meta:
        model = Forecast
        fields = (
            'store',
            'forecast_date',
            'forecast'
        )

    def get_forecast_date(self, obj):
        """Получаем текущую дату в момент запроса."""

        return date.today()

    def create(self, validated_data):
        """Записываем полученный JSON в БД."""

        store_name = validated_data['store']
        forecast_data = validated_data['forecast']

        sku = forecast_data['sku']
        sales_units_data = forecast_data['sales_units']

        shop = Shop.objects.get(st_id=store_name)
        product = SKU.objects.get(pr_sku_id=sku)

        for date, target in sales_units_data.items():
            Forecast.objects.create(
                st_id=shop,
                pr_sku_id=product,
                target=target,
                date=date
            )

        return validated_data

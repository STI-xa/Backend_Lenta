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
        source='st_division_code_id'
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


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза."""

    store = serializers.CharField(source='st_id')
    forecast_date = serializers.DateField(source='date')
    forecast = serializers.JSONField()

    class Meta:
        model = Forecast
        fields = ('store', 'forecast_date', 'forecast')

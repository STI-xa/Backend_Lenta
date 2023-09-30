from rest_framework import serializers

from backend.logger import log_exceptions, logger_factory
from sales.models import SKU, Shop, Sales, Forecast


logger = logger_factory(__name__)


@log_exceptions(logger)
class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = (
            'pr_sku_id',
            'pr_group_id',
            'pr_cat_id',
            'pr_subcat_id',
            'pr_uom_id')


@log_exceptions(logger)
class ForecastEntrySerializer(serializers.Serializer):
    date = serializers.DateField()
    sales_type = serializers.IntegerField(source='pr_sales_type_id')
    sales_units = serializers.DecimalField(
        max_digits=6, decimal_places=1, source='pr_sales_in_units')
    sales_units_promo = serializers.DecimalField(
        max_digits=6, decimal_places=1, source='pr_promo_sales_in_units')
    sales_rub = serializers.DecimalField(
        max_digits=8, decimal_places=1, source='pr_sales_in_rub')
    sales_run_promo = serializers.DecimalField(
        max_digits=8, decimal_places=1, source='pr_promo_sales_in_rub')


@log_exceptions(logger)
class ForecastSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='st_id.st_id')
    sku = serializers.CharField(source='pr_sku_id.pr_sku_id')
    fact = ForecastEntrySerializer(many=True)

    class Meta:
        model = Forecast
        fields = ('store', 'sku', 'fact')


@log_exceptions(logger)
class CategorySerializer(serializers.ModelSerializer):
    sku = serializers.CharField(source='pr_sku_id.pr_sku_id')
    group = serializers.CharField(source='pr_group_id')
    category = serializers.CharField(source='pr_cat_id')
    subcategory = serializers.CharField(source='pr_subcat_id')
    uom = serializers.IntegerField(source='pr_uom_id')

    class Meta:
        model = SKU
        fields = ('sku', 'group', 'category', 'subcategory', 'uom')


@log_exceptions(logger)
class SalesDataSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='st_id.st_id')
    sku = serializers.CharField(source='pr_sku_id.pr_sku_id')
    fact = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = ('store', 'sku', 'fact')

    def get_fact(self, obj):
        return SalesSerializer(obj.sales_store.all(), many=True).data


@log_exceptions(logger)
class SalesSerializer(serializers.Serializer):
    data = SalesDataSerializer(many=True)


@log_exceptions(logger)
class ShopSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='st_id')
    city = serializers.CharField(source='st_city_id')
    division = serializers.CharField(source='st_division_code_id')
    type_format = serializers.IntegerField(source='st_type_format_id')
    loc = serializers.IntegerField(source='st_type_loc_id')
    size = serializers.IntegerField(source='st_type_size_id')
    is_active = serializers.BooleanField(source='st_is_active')

    class Meta:
        model = Shop
        fields = ('store',
                  'city',
                  'division',
                  'type_format',
                  'loc',
                  'size',
                  'is_active')


@log_exceptions(logger)
class ForecastEntryInputSerializer(serializers.Serializer):
    date = serializers.DateField()
    sales_units = serializers.DecimalField(max_digits=6, decimal_places=1)


@log_exceptions(logger)
class ForecastInputSerializer(serializers.Serializer):
    store = serializers.CharField()
    forecast_date = serializers.DateField()
    forecast = serializers.DictField(child=ForecastEntryInputSerializer())


@log_exceptions(logger)
class ForecastEntryOutputSerializer(serializers.Serializer):
    date = serializers.DateField()
    sales_units = serializers.DecimalField(max_digits=6, decimal_places=1)


@log_exceptions(logger)
class ForecastOutputSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='st_id.st_id')
    forecast_date = serializers.DateField(source='date')
    forecast = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = ('store', 'forecast_date', 'forecast')

    def get_forecast(self, obj):
        forecast_entries = obj.store_forecast.filter(date=obj.date)
        return ForecastEntryOutputSerializer(forecast_entries, many=True).data

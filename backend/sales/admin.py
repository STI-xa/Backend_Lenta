from django.contrib import admin
from .models import SKU, Shop, Sales, Forecast


@admin.register(SKU)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('sku_id', 'group', 'category', 'subcategory', 'uom')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'store_id',
        'city', 'division', 'type_format', 'loc', 'size', 'is_active')


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'store_id', 'sku_id', 'date', 'sales_type', 'sales_units',
        'sales_units_promo', 'sales_rub', 'sales_run_promo')


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'sku_id', 'forecast_date', 'forecast')

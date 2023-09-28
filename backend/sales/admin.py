from django.contrib import admin
from .models import Category, Shop, Sales, Forecast


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('sku', 'group', 'category', 'subcategory', 'uom')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'store', 'city', 'division', 'type_format', 'loc', 'size', 'is_active')


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('store', 'sku')


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('store', 'sku', 'forecast_date')

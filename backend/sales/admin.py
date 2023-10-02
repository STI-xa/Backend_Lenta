from django.contrib import admin
from .models import SKU, Shop, Sales, Forecast


@admin.register(SKU)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pr_sku_id',
        'pr_group_id',
        'pr_cat_id',
        'pr_subcat_id',
        'pr_uom_id'
    )


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'st_id',
        'st_city_id',
        'st_division_code',
        'st_type_format_id',
        'st_type_loc_id',
        'st_type_size_id',
        'st_is_active'
    )


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'st_id',
        'pr_sku_id',
        'date',
        'pr_sales_type_id',
        'pr_sales_in_units',
        'pr_promo_sales_in_units',
        'pr_sales_in_rub',
        'pr_promo_sales_in_rub'
    )


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = (
        'st_id',
        'pr_sku_id',
        'date',
        'target'
    )

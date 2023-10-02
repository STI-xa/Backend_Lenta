from django.db import models


class SKU(models.Model):
    """Модель с товарной иерархией."""

    pr_sku_id = models.CharField(
        primary_key=True,
        max_length=150,
        verbose_name='Товар',
        db_index=True,
    )
    pr_group_id = models.CharField(
        max_length=150,
        verbose_name='Группа товара',
    )
    pr_cat_id = models.CharField(
        max_length=150,
        verbose_name='Категория товара',
    )
    pr_subcat_id = models.CharField(
        max_length=150,
        verbose_name='Подкатегория товара',
    )
    pr_uom_id = models.IntegerField(
        verbose_name='Единицы измерения',
    )

    def __str__(self):
        return self.pr_sku_id

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Shop(models.Model):
    """Модель с информацией о ТЦ."""

    st_id = models.CharField(
        primary_key=True,
        max_length=150,
        verbose_name='Магазин',
        db_index=True,
    )
    st_city_id = models.CharField(
        max_length=150,
        verbose_name='Город',
    )
    st_division_code_id = models.CharField(
        max_length=150,
        verbose_name='Дивизион',
    )
    st_type_format_id = models.IntegerField(
        verbose_name='Формат магазина',
    )
    st_type_loc_id = models.IntegerField(
        verbose_name='Тип локации',
    )
    st_type_size_id = models.IntegerField(
        verbose_name='Размер магазина',
    )
    st_is_active = models.BooleanField(
        verbose_name='Флаг активности',
    )

    def __str__(self):
        return self.st_id

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Sales(models.Model):
    """Модель с продажами определённой позиции товара."""

    st_id = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='sales_store',
        verbose_name='Магазин',
    )
    pr_sku_id = models.ForeignKey(
        SKU,
        on_delete=models.CASCADE,
        related_name='sales_sku',
        verbose_name='Товар',
    )
    date = models.DateField(
        verbose_name='Дата продаж',
    )
    pr_sales_type_id = models.IntegerField(
        verbose_name='Флаг наличия промо',
    )
    pr_sales_in_units = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name='Число проданных товаров без промо',
    )
    pr_promo_sales_in_units = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name='Число проданных товаров c промо',
    )
    pr_sales_in_rub = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        verbose_name='Продажи без промо в руб',
    )
    pr_promo_sales_in_rub = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        verbose_name='Продажи c промо в руб',
    )

    def __str__(self):
        return f'Продажи {self.pr_sku_id} в {self.st_id} - {self.date}'

    class Meta:
        verbose_name = 'Продажи определённой позиции'
        verbose_name_plural = 'Продажи определённой позиции'
        ordering = ('-date',)


class Forecast(models.Model):
    st_id = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='store_forecast',
        verbose_name='магазин',
    )
    pr_sku_id = models.ForeignKey(
        SKU,
        on_delete=models.CASCADE,
        related_name='sku_forecast',
        verbose_name='товар',
    )
    date = models.DateField()
    target = models.IntegerField(verbose_name='Спрос в шт',)

    def __str__(self):
        return f'Прогноз продаж: {self.pr_sku_id}в\
            {self.st_id} {self.date}'

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'

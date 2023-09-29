from django.db import models


class SKU(models.Model):
    sku_id = models.CharField(
        primary_key=True,
        max_length=150,
        verbose_name='Товар',
        db_index=True,
    )
    group = models.CharField(
        max_length=150,
        verbose_name='Группа',
    )
    category = models.CharField(
        max_length=150,
        verbose_name='Категория',
    )
    subcategory = models.CharField(
        max_length=150,
        verbose_name='Подкатегория',
    )
    uom = models.IntegerField(verbose_name='Единицы измерения',)

    def __str__(self):
        return self.sku_id

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Shop(models.Model):
    store_id = models.CharField(
        primary_key=True,
        max_length=150,
        verbose_name='Магазин',
        db_index=True,
    )
    city = models.CharField(
        max_length=150,
        verbose_name='Город',
    )
    division = models.CharField(
        max_length=150,
        verbose_name='Дивизион',
    )
    type_format = models.IntegerField(verbose_name='Формат',)
    loc = models.IntegerField(verbose_name='Тип локации',)
    size = models.IntegerField(verbose_name='Размер',)
    is_active = models.BooleanField(verbose_name='Активность',)

    def __str__(self):
        return self.store_id

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Sales(models.Model):
    store_id = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='sales_store',
        verbose_name='магазин',
    )
    sku_id = models.ForeignKey(
        SKU,
        on_delete=models.CASCADE,
        related_name='sales_sku',
        verbose_name='товар',
    )
    date = models.DateField(verbose_name='дата продаж',)
    sales_type = models.IntegerField(verbose_name='тип продаж',)
    sales_units = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name='всего шт',
    )
    sales_units_promo = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name='промо шт',
    )
    sales_rub = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        verbose_name='всего руб',
    )
    sales_run_promo = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        verbose_name='промо руб',
    )

    def __str__(self):
        return f'Продажи: {self.sku_id} в {self.store_id}'

    class Meta:
        verbose_name = 'Продажи'
        ordering = ('-date',)


class Forecast(models.Model):
    store_id = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
        related_name='sales_store',
        verbose_name='магазин',
    )
    sku_id = models.ForeignKey(
        SKU,
        on_delete=models.CASCADE,
        related_name='sales_sku',
        verbose_name='товар',
    )
    forecast_date = models.DateField()
    forecast = models.ForeignKey(
        Sales,
        on_delete=models.CASCADE,
        related_name='forecast_sales_units',
        verbose_name='всего шт',
    )

    def __str__(self):
        return f'Прогноз продаж: {self.sku_id}в\
            {self.store_id} {self.forecast_date}'

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'

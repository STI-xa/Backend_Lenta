from django.db import models


class Category(models.Model):
    sku = models.CharField(max_length=150)
    group = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    subcategory = models.CharField(max_length=150)
    uom = models.IntegerField()

    def __str__(self):
        return self.category


class Shop(models.Model):
    store = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    division = models.CharField(max_length=150)
    type_format = models.IntegerField()
    loc = models.IntegerField()
    size = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.store


class Sales(models.Model):
    store = models.ForeignKey(Shop, on_delete=models.CASCADE)
    sku = models.CharField(max_length=150)

    def __str__(self):
        return f'Продажи: {self.sku} в {self.store}'


class Forecast(Sales):
    forecast_date = models.DateField()
    forecast = models.JSONField()
    sales_units = models.JSONField()

    def __str__(self):
        return f'Прогноз продаж: {self.sku}в\
            {self.store} {self.forecast_date}'

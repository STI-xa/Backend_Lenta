from django.db import models


class Store(models.Model):
    st_id = models.CharField(max_length=100, primary_key=True)
    st_city_id = models.CharField(max_length=100)
    st_division_code = models.CharField(max_length=100)
    st_type_format_id = models.CharField(max_length=100)
    st_type_loc_id = models.CharField(max_length=100)
    st_type_size_id = models.CharField(max_length=100)
    st_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.st_id


class ProductGroup(models.Model):
    pr_group_id = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.pr_group_id


class ProductCategory(models.Model):
    pr_cat_id = models.CharField(max_length=100, primary_key=True)
    pr_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.pr_cat_id


class ProductSubcategory(models.Model):
    pr_subcat_id = models.CharField(max_length=100, primary_key=True)
    pr_cat = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.pr_subcat_id


class Product(models.Model):
    pr_sku_id = models.CharField(max_length=100, primary_key=True)
    pr_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    pr_cat = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    pr_subcat = models.ForeignKey(ProductSubcategory, on_delete=models.CASCADE)
    pr_uom_id = models.CharField(max_length=100)

    def __str__(self):
        return self.pr_sku_id


class CommonFields(models.Model):
    st = models.ForeignKey(Store, on_delete=models.CASCADE)
    pr_sku = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        abstract = True


class Sales(CommonFields):
    pr_sales_type_id = models.BooleanField()
    pr_sales_in_units = models.IntegerField()
    pr_promo_sales_in_units = models.IntegerField()
    pr_sales_in_rub = models.FloatField()
    pr_promo_sales_in_rub = models.FloatField()


class SalesSubmission(CommonFields):
    target = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.st} - {self.pr_sku}'

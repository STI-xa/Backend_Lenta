from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_username


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username'
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[validate_username]
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
    )
    password = models.CharField(
        'Пароль',
        max_length=150,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user'),
        ]


class CommonFields(models.Model):
    st_id = models.CharField(max_length=100)
    pr_sku_id = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        abstract = True


class SalesDFTrain(CommonFields):
    pr_sales_type_id = models.IntegerField()
    pr_sales_in_units = models.IntegerField()
    pr_promo_sales_in_units = models.IntegerField()
    pr_sales_in_rub = models.FloatField()
    pr_promo_sales_in_rub = models.FloatField()


class PRDF(CommonFields):
    pr_group_id = models.CharField(max_length=100)
    pr_cat_id = models.CharField(max_length=100)
    pr_subcat_id = models.CharField(max_length=100)
    pr_uom_id = models.CharField(max_length=100)

    @property
    def specific_field(self):
        return super().pr_sku_id


class PRST(CommonFields):
    st_city_id = models.CharField(max_length=100)
    st_division_code_id = models.CharField(max_length=100)
    st_type_format_id = models.IntegerField()
    st_type_loc_id = models.IntegerField()
    st_type_size_id = models.IntegerField()
    st_is_active = models.BooleanField()

    @property
    def specific_field(self):
        return super().st_id


class SalesSubmission(CommonFields):
    target = models.IntegerField(default=0)

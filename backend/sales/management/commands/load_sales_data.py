import os
from datetime import datetime

import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction

from sales.models import SKU, Shop, Sales


# Данные этой модели должны быть загружены только после данных SKU и Shop
class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(
            os.path.dirname(__file__), 'sales_df_train.csv')

        df = pd.read_csv(file_path)

        sales_records = []
        with transaction.atomic():
            for _, row in df.iterrows():
                shop = Shop.objects.get(st_id=row['st_id'])
                sku = SKU.objects.get(pr_sku_id=row['pr_sku_id'])
                date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                sales = Sales(
                    st_id=shop,
                    pr_sku_id=sku,
                    date=date,
                    pr_sales_type_id=row['pr_sales_type_id'],
                    pr_sales_in_units=row['pr_sales_in_units'],
                    pr_promo_sales_in_units=row['pr_promo_sales_in_units'],
                    pr_sales_in_rub=row['pr_sales_in_rub'],
                    pr_promo_sales_in_rub=row['pr_promo_sales_in_rub']
                )
                sales_records.append(sales)
            
            Sales.objects.bulk_create(sales_records)

        self.stdout.write(self.style.SUCCESS('Данные Sales загружены успешно'))

import csv
import os

from django.core.management.base import BaseCommand
from sales.models import SKU


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'pr_df.csv')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sku = SKU(
                    pr_sku_id=row['pr_sku_id'],
                    pr_group_id=row['pr_group_id'],
                    pr_cat_id=row['pr_cat_id'],
                    pr_subcat_id=row['pr_subcat_id'],
                    pr_uom_id=row['pr_uom_id']
                )
                sku.save()

        self.stdout.write(self.style.SUCCESS('Данные SKU загружены успешно'))

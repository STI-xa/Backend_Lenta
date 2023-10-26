import os

import pandas as pd
from django.core.management.base import BaseCommand

from sales.models import Shop


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(
            os.path.dirname(__file__), 'st_df.csv')

        df = pd.read_csv(file_path)

        shop_records = []
        for _, row in df.iterrows():
            shop = Shop(
                st_id=row['st_id'],
                st_city_id=row['st_city_id'],
                st_division_code=row['st_division_code'],
                st_type_format_id=row['st_type_format_id'],
                st_type_loc_id=row['st_type_loc_id'],
                st_type_size_id=row['st_type_size_id'],
                st_is_active=row['st_is_active']
            )
            shop_records.append(shop)

        Shop.objects.bulk_create(shop_records)

        self.stdout.write(self.style.SUCCESS('Данные Shop загружены успешно'))

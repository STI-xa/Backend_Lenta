import csv
import os

from django.core.management.base import BaseCommand
from sales.models import Shop


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'st_df.csv')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                shop = Shop(
                    st_id=row['st_id'],
                    st_city_id=row['st_city_id'],
                    st_division_code=row['st_division_code'],
                    st_type_format_id=row['st_type_format_id'],
                    st_type_loc_id=row['st_type_loc_id'],
                    st_type_size_id=row['st_type_size_id'],
                    st_is_active=row['st_is_active']
                )
                shop.save()

        self.stdout.write(self.style.SUCCESS('Данные Shop загружены успешно'))

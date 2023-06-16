from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [

            {
                "name": "Продукты",
                "description": null

            },
            {
                "name": "Техника",
                "description": null

            },
            {
                "name": "Товары для спорта",
                "description": null
            },
        ]

        category_object = []

        for category_item in category_list:
            category_object.append(Category(**category_item))

        Category.objects.bulk_create(category_object)

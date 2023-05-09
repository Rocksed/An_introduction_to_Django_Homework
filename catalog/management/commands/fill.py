from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {
                "name": "Помидор",
                "description": "Красный",
                "image_preview": "",
                "category": "Овощи",
                "purchase_price": 150,
            },
        ]
        product_object = []
        for product_item in product_list:
            product_object.append(Product(**product_item))

        Product.objects.bulk_create(product_object)

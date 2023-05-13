from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {
                "name": "Огурец",
                "description": "Парниковый",
                "image_preview": "media/image/white.jpg",
                "category": "Овощи",
                "purchase_price": 199,
                "creation_date": "2023-05-13T13:06:12Z",
                "last_modified_date": "2023-05-13T13:06:13Z"
            },
            {
                "name": "Томаты",
                "description": "Парниковые",
                "image_preview": "media/image/tomatoes.jpg",
                "category": "Овощи",
                "purchase_price": 299,
                "creation_date": "2023-05-13T13:08:17Z",
                "last_modified_date": "2023-05-13T13:08:18Z"
            },
            {
                "name": "Яблок",
                "description": "Польский",
                "image_preview": "media/image/depositphotos_107748126-stock-photo-fresh-red-apple-with-leaf.jpg",
                "category": "Фрукт",
                "purchase_price": 99,
                "creation_date": "2023-05-13T13:09:42Z",
                "last_modified_date": "2023-05-13T13:09:43Z"
            },
            {
                "name": "Торт",
                "description": "Свежий",
                "image_preview": "media/image/depositphotos_11726181-stock-photo-weddind-cake-with-flowers-over.jpg",
                "category": "Кондитерские изделия",
                "purchase_price": 599,
                "creation_date": "2023-05-13T13:10:25Z",
                "last_modified_date": "2023-05-13T13:10:26Z"
            }
        ]
        product_object = []
        for product_item in product_list:
            product_object.append(Product(**product_item))

        Product.objects.bulk_create(product_object)

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image_preview = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description} {self.category}'

    class Meta:
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        ordering = ('name',)

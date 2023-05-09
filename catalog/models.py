from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    image_preview = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория', **NULLABLE)
    purchase_price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description} {self.category}'

    class Meta:
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        ordering = ('name',)

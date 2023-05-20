from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    image_preview = models.ImageField(upload_to='media/image/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория', **NULLABLE)
    purchase_price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description} {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Blog(models.Model):
    headline = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='slug', **NULLABLE)
    content = models.TextField(max_length=1000, verbose_name='Содержание', **NULLABLE)
    preview = models.ImageField(upload_to='media/image/', verbose_name='Изображение', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    publication_feature = models.CharField(max_length=50, verbose_name='Признак публикации')
    views_count = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.headline} {self.slug} {self.content} {self.publication_feature}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ('views_count',)

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    image_preview = models.ImageField(upload_to='media/image/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description} {self.category}'

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[str(self.pk)])

    def get_latest_version(self):
        active_version = self.version_set.filter(is_active=True).first()
        if active_version:
            return active_version
        else:
            return self.version_set.order_by('-version_number').first()

    def is_editable_by(self, user):
        return self.owner == user

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Blog(models.Model):
    headline = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=50, verbose_name='slug', **NULLABLE)
    content = models.TextField(max_length=1000, verbose_name='Содержание', **NULLABLE)
    preview = models.ImageField(upload_to='media/image/', verbose_name='Изображение', **NULLABLE)
    creation_date_blog = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    publication_feature = models.CharField(max_length=50, verbose_name='Признак публикации', **NULLABLE)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.headline} {self.slug} {self.content} {self.publication_feature}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
        ordering = ('views_count',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='Номер версии', **NULLABLE)
    version_name = models.CharField(verbose_name='Название версии', max_length=255, **NULLABLE)
    is_active = models.BooleanField(verbose_name='Признак текущей версии', default=False, **NULLABLE)

    def __str__(self):
        return f"{self.product.name} - {self.version_number} - {self.version_name}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версия'

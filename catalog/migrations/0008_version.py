# Generated by Django 4.2 on 2023-06-05 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_blog_views_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=255, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=False, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
# Generated by Django 4.2 on 2023-06-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_version_version_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Признак текущей версии'),
        ),
    ]

# Generated by Django 4.2 on 2023-05-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_blog_publication_feature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]

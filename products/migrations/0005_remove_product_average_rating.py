# Generated by Django 3.2 on 2022-01-29 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220129_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='average_rating',
        ),
    ]

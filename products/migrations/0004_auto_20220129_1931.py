# Generated by Django 3.2 on 2022-01-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]

# Generated by Django 3.2.1 on 2021-05-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210506_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchhistory',
            name='search',
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='url',
            field=models.URLField(default='http://localhost:8000/products/1'),
            preserve_default=False,
        ),
    ]
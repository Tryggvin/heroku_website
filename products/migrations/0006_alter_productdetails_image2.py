# Generated by Django 3.2.1 on 2021-05-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productdetails_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='image2',
            field=models.CharField(blank=True, default='', max_length=9999, null=True),
        ),
    ]

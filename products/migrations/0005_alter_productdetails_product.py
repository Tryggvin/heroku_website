# Generated by Django 3.2.1 on 2021-05-12 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_productdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
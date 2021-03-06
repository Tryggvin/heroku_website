# Generated by Django 3.2.1 on 2021-05-11 21:32

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_payment_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('streetName', models.CharField(max_length=100, null=True)),
                ('houseNumber', models.PositiveSmallIntegerField()),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postalCode', models.PositiveSmallIntegerField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.customer')),
            ],
        ),
    ]

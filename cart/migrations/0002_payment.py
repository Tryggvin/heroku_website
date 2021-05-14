
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardOwner', models.CharField(max_length=100, null=True)),
                ('cardNumber', models.CharField(max_length=19, null=True)),
                ('expirationDateMonth', models.CharField(max_length=2, null=True)),
                ('expirationDateYear', models.CharField(max_length=2, null=True)),
                ('cvc', models.CharField(max_length=3, null=True)),
                ('user', models.OneToOneField( unique=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.customer')),
            ],
        ),
    ]

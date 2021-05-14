
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20210511_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='month',
        ),
    ]

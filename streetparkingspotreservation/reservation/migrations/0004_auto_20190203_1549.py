# Generated by Django 2.1.5 on 2019-02-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20190203_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspots',
            name='lat',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='parkingspots',
            name='lng',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]

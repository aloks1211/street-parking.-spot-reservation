# Generated by Django 2.1.5 on 2019-02-03 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=5, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=8, max_digits=10)),
                ('reserved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.ParkingSpots')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=128)),
                ('last_name', models.CharField(default=None, max_length=128)),
                ('contact', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservations',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.User'),
        ),
    ]

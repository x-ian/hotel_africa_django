# Generated by Django 3.0.2 on 2020-01-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0016_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.IntegerField(blank=True),
        ),
    ]

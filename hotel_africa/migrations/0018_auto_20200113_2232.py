# Generated by Django 3.0.2 on 2020-01-13 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0017_auto_20200113_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitrate',
            name='payment_cash',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitrate',
            name='payment_creditcard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitrate',
            name='payment_paypal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitrate',
            name='payment_westernunion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitrate',
            name='payment_wiretransfer',
            field=models.BooleanField(default=False),
        ),
    ]
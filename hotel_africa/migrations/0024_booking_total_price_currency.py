# Generated by Django 3.0.2 on 2020-01-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0023_auto_20200115_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price_currency',
            field=models.CharField(choices=[('USD (USA)', 'Usd'), ('EUR (Europe)', 'Eur'), ('XOF (CFA Franc)', 'Xof'), ('NGN (Nigeria)', 'Ngn'), ('MWK (Malawi)', 'Mwk')], default='USD (USA)', max_length=25),
        ),
    ]
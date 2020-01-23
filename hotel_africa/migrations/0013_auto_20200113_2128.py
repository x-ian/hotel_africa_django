# Generated by Django 3.0.2 on 2020-01-13 21:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0012_auto_20200111_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('rate_currency', models.CharField(choices=[('USD (USA)', 'Usd'), ('EUR (Europe)', 'Eur'), ('XOF (CFA Franc)', 'Xof'), ('NGN (Nigeria)', 'Ngn'), ('MWK (Malawi)', 'Mwk')], default='USD (USA)', max_length=25)),
                ('rate_standard', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rate_early_booker', models.DecimalField(decimal_places=2, max_digits=6)),
                ('free_cancellation', models.BooleanField()),
                ('rate_cancellation', models.DecimalField(decimal_places=2, max_digits=6)),
                ('special_offers', models.TextField(blank=True, default='', max_length=1024)),
                ('meals', models.TextField(blank=True, default='', max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='checkin_from',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facility',
            name='checkout_at',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

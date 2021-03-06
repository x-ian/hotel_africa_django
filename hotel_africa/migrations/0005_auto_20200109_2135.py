# Generated by Django 3.0.2 on 2020-01-09 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0004_auto_20200109_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='facility',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Facility'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='quantity_of_units_in_facility',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FacilityUnit',
        ),
    ]

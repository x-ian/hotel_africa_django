# Generated by Django 3.0.2 on 2020-01-08 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0002_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='FacilityUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Facility')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='FacilityPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Facility')),
            ],
        ),
    ]
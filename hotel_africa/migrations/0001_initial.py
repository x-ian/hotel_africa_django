# Generated by Django 3.0.2 on 2020-01-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('arrival', models.TextField(max_length=1024)),
                ('address_street_1', models.CharField(max_length=100)),
                ('address_street_2', models.CharField(max_length=100)),
                ('address_city', models.CharField(max_length=100)),
                ('address_zip', models.CharField(max_length=100)),
                ('address_state', models.CharField(max_length=100)),
                ('address_country', models.CharField(max_length=100)),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_phone_1', models.CharField(max_length=100)),
                ('contact_phone_2', models.CharField(max_length=100)),
                ('contact_phone_3', models.CharField(max_length=100)),
                ('policies', models.TextField(max_length=1024)),
                ('directions', models.TextField(max_length=1024)),
                ('speciality_beach', models.BooleanField()),
                ('speciality_swimming_pool', models.BooleanField()),
                ('speciality_fitness_room', models.BooleanField()),
                ('speciality_bar', models.BooleanField()),
                ('speciality_restaurant_meal_breakfast', models.BooleanField()),
                ('speciality_restaurant_meal_dinner', models.BooleanField()),
                ('speciality_restaurant_meal_lunch', models.BooleanField()),
                ('speciality_restaurant_prices', models.TextField(max_length=1024)),
                ('speciality_restaurant_times', models.TextField(max_length=1024)),
                ('speciality_kids_playground', models.BooleanField()),
                ('speciality_airport_shuttle', models.BooleanField()),
                ('speciality_24h_front_desk', models.BooleanField()),
                ('speciality_extras', models.TextField(max_length=1024)),
                ('languages', models.TextField(max_length=1024)),
                ('parking', models.BooleanField()),
                ('cleaning_laundry', models.BooleanField()),
                ('cleaning_housekeeping', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-17 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0032_auto_20200117_0437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='kind',
            new_name='type',
        ),
    ]

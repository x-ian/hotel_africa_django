# Generated by Django 3.0.2 on 2020-01-15 16:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_africa', '0027_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='refer_booking',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Booking'),
        ),
        migrations.AlterField(
            model_name='message',
            name='refer_facility',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Facility'),
        ),
        migrations.AlterField(
            model_name='message',
            name='refer_unit',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Unit'),
        ),
    ]

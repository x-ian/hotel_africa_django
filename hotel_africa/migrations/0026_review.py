# Generated by Django 3.0.2 on 2020-01-15 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_africa', '0025_auto_20200115_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('review_text', models.TextField(blank=True, default='', max_length=1024)),
                ('review_rating', models.CharField(choices=[('1/5', 'One'), ('2/5', 'Two'), ('3/5', 'Three'), ('4/5', 'Four'), ('5/5', 'Five')], max_length=5)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_africa.Booking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

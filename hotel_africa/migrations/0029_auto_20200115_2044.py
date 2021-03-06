# Generated by Django 3.0.2 on 2020-01-15 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_africa', '0028_auto_20200115_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='language',
            field=models.CharField(choices=[('german', 'De'), ('french', 'Fr'), ('english', 'En'), ('spanish', 'Es')], default='DE', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]

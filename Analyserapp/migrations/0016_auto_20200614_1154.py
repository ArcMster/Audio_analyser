# Generated by Django 3.0.2 on 2020-06-14 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyserapp', '0015_output_audios_rmse'),
    ]

    operations = [
        migrations.AddField(
            model_name='output_audios',
            name='end_time',
            field=models.IntegerField(default=456),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='output_audios',
            name='start_time',
            field=models.IntegerField(default=546),
            preserve_default=False,
        ),
    ]
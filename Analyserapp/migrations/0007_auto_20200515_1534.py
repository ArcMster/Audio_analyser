# Generated by Django 3.0.2 on 2020-05-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyserapp', '0006_output_audios_visual_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='output_audios',
            name='visual_2',
            field=models.FileField(default='default', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='output_audios',
            name='visual_3',
            field=models.FileField(default='default', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='output_audios',
            name='visual_4',
            field=models.FileField(default='default', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='output_audios',
            name='visual_5',
            field=models.FileField(default='default', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='output_audios',
            name='visual_6',
            field=models.FileField(default='default', upload_to='media'),
            preserve_default=False,
        ),
    ]

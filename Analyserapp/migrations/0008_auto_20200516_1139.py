# Generated by Django 3.0.2 on 2020-05-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyserapp', '0007_auto_20200515_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_audios',
            name='visual_1',
            field=models.FileField(default='sample', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input_audios',
            name='visual_2',
            field=models.FileField(default='sample', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input_audios',
            name='visual_3',
            field=models.FileField(default='sample', upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input_audios',
            name='visual_4',
            field=models.FileField(default='sample', upload_to='media'),
            preserve_default=False,
        ),
    ]

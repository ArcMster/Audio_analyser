# Generated by Django 3.0.2 on 2020-05-10 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input_audios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_1', models.FileField(upload_to='media')),
                ('audio_2', models.FileField(upload_to='media')),
                ('audio_3', models.FileField(upload_to='media')),
                ('audio_analyse', models.FileField(upload_to='media')),
                ('search_1', models.FileField(upload_to='media')),
                ('search_2', models.FileField(upload_to='media')),
                ('search_3', models.FileField(upload_to='media')),
                ('search_4', models.FileField(upload_to='media')),
                ('search_5', models.FileField(upload_to='media')),
                ('search_6', models.FileField(upload_to='media')),
            ],
        ),
    ]

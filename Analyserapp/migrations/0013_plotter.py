# Generated by Django 3.0.2 on 2020-05-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyserapp', '0012_output_audios_runtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plotter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(max_length=20)),
                ('window_size', models.IntegerField()),
                ('runtime', models.IntegerField()),
            ],
        ),
    ]
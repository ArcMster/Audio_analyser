# Generated by Django 3.0.2 on 2020-05-10 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyserapp', '0002_auto_20200510_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media')),
                ('aud1_response', models.TextField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-27 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotos_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotos',
            name='data_fotografia',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 3.2.5 on 2021-12-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icoproject',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

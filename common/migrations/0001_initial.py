# Generated by Django 4.0 on 2022-01-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=50)),
                ('currency_abbr', models.CharField(max_length=3, unique=True)),
                ('currency_sign', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 4.0 on 2022-01-20 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_country_country_code'),
        ('equities', '0013_alter_equityproject_sector_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='equityproject',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.country', to_field='country_code'),
        ),
    ]
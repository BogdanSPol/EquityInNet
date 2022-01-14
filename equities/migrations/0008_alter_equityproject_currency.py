# Generated by Django 4.0 on 2022-01-12 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('equities', '0007_alter_equityproject_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equityproject',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='currencies', to='common.currencies', to_field='currency_abbr'),
        ),
    ]

# Generated by Django 4.0 on 2022-01-12 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_sectorchoices'),
        ('equities', '0012_alter_equityproject_sector_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equityproject',
            name='sector_choice',
            field=models.ForeignKey(default='NONE', help_text='In classification of yahoo.finance', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.sectorchoices', to_field='sector_name'),
        ),
    ]
# Generated by Django 4.2 on 2023-04-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_app', '0002_rename_name_costs_summa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costs',
            old_name='category',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='category',
            new_name='categories',
        ),
        migrations.AlterField(
            model_name='income',
            name='income_date',
            field=models.DateTimeField(),
        ),
    ]

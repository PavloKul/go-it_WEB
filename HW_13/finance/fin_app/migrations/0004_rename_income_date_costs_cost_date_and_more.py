# Generated by Django 4.2 on 2023-05-04 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin_app', '0003_rename_category_costs_categories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='costs',
            old_name='income_date',
            new_name='cost_date',
        ),
        migrations.RenameField(
            model_name='coststocategory',
            old_name='costs',
            new_name='cost',
        ),
    ]

# Generated by Django 3.0.8 on 2021-01-07 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='updates_at',
            new_name='updated_at',
        ),
    ]

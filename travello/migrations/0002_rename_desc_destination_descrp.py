# Generated by Django 4.2.6 on 2023-10-25 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='desc',
            new_name='descrp',
        ),
    ]
